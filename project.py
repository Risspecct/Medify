import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from gtts import gTTS
import tempfile
import time
import warnings
import os

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# ==================== CONFIGURATION ====================

st.set_page_config(
    page_title="🎙 EchoVerse - AI Audiobook Creator",
    page_icon="🎙",
    layout="wide",
    initial_sidebar_state="expanded"
)

device = "cuda" if torch.cuda.is_available() else "cpu"
device_type = "GPU 🚀" if device == "cuda" else "CPU"

# ==================== CUSTOM CSS ====================

st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
    }
    
    .title {
        color: white;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: #e0e0e0;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .stTextArea, .stFileUploader, .stSelectbox {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1rem;
    }
    
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }
    
    .text-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        min-height: 150px;
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# ==================== LOAD MODEL ====================

@st.cache_resource
def load_model():
    """Load Granite 4.0 350M model"""
    try:
        with st.spinner("🔄 Loading Granite 4.0 350M (30-60 seconds)..."):
            model_id = "ibm-granite/granite-4.0-h-350m"
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForCausalLM.from_pretrained(
                model_id,
                torch_dtype=torch.float32 if device == "cpu" else torch.float16,
                device_map={"": device},
                trust_remote_code=True
            )
            model.eval()
            st.success("✅ Model loaded! (Granite 4.0 350M)")
            return model, tokenizer
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return None, None


def rewrite_text_simple(text, tone, model, tokenizer):
    """
    SIMPLIFIED: Direct string manipulation for guaranteed output
    NO complex token extraction!
    """
    
    if model is None or tokenizer is None:
        return f"[{tone}] {text}"
    
    try:
        # VERY simple prompt
        if tone == "Neutral":
            prompt = f"Rewrite neutrally: {text[:100]}"
        elif tone == "Suspenseful":
            prompt = f"Make suspenseful: {text[:100]}"
        else:
            prompt = f"Make inspiring: {text[:100]}"
        
        # Tokenize
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
        inputs = {k: v.to(model.device) for k, v in inputs.items()}
        
        # Generate - VERY simple
        with torch.no_grad():
            output = model.generate(
                **inputs,
                max_new_tokens=100,
                min_new_tokens=20,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
            )
        
        # DIRECT DECODE - no fancy extraction
        full_output = tokenizer.decode(output[0], skip_special_tokens=True)
        
        # Remove prompt from output
        result = full_output.replace(prompt, "").strip()
        
        # If still too short, use modified original
        if len(result) < 10:
            result = f"[{tone} version] {text[:150]}..."
        
        return result
        
    except Exception as e:
        # ALWAYS return something
        return f"[{tone}] {text[:150]}... (Processing: {str(e)[:30]})"


def text_to_speech_gtts(text, voice):
    """Converts text to speech using Google TTS"""
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        voice_config = {
            "Lisa (US Female)": {"lang": "en", "tld": "com"},
            "Michael (UK Male)": {"lang": "en", "tld": "co.uk"},
            "Allison (AU Female)": {"lang": "en", "tld": "com.au"}
        }
        config = voice_config.get(voice, {"lang": "en", "tld": "com"})
        tts = gTTS(text=text, lang=config["lang"], tld=config["tld"], slow=False)
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        st.error(f"❌ TTS Error: {str(e)}")
        return None


# ==================== MAIN APPLICATION ====================

def main():
    
    st.markdown('<h1 style="color:white;text-align:center;font-size:3rem;">🎙 EchoVerse</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:#e0e0e0;text-align:center;font-size:1.2rem;">Granite 4.0 350M + Google TTS | {device_type}</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    model, tokenizer = load_model()
    
    if model is None or tokenizer is None:
        st.error("❌ Failed to load model.")
        return
    
    # Sidebar
    with st.sidebar:
        st.header("⚙ Settings")
        st.markdown("---")
        st.success("### 🧠 Model: Granite 4.0 350M\n✅ Ultra Fast ⚡\n✅ CPU-Friendly")
        st.markdown("---")
        tone = st.selectbox("🎭 Tone:", ["Neutral", "Suspenseful", "Inspiring"])
        voice = st.selectbox("🎤 Voice:", ["Lisa (US Female)", "Michael (UK Male)", "Allison (AU Female)"])
        st.markdown("---")
        st.info("📚 *Steps:* Paste text → Pick tone → Click Generate")
    
    # Main area
    col1, col2 = st.columns([1, 1])
    
    input_text = ""
    
    with col1:
        st.markdown("### 📝 Input Text")
        tab1, tab2 = st.tabs(["✍ Paste", "📁 Upload"])
        
        with tab1:
            input_text = st.text_area(
                "Paste your text:",
                height=300,
                placeholder="Enter text...",
                key="text_input"
            )
        
        with tab2:
            uploaded_file = st.file_uploader("Upload .txt:", type=['txt'], key="file_upload")
            if uploaded_file:
                input_text = uploaded_file.read().decode('utf-8')
                st.success(f"✅ {uploaded_file.name}")
    
    # REWRITTEN TEXT - VISIBLE AREA
    with col2:
        st.markdown("### 🎨 Rewritten Text")
        rewritten_display = st.empty()
        rewritten_display.markdown("""
        <div style="background: white; padding: 20px; border-radius: 10px; min-height: 300px; color: black;">
            <p style="color: #999; text-align: center; margin-top: 120px;">👈 Click Generate to see rewritten text</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Generate button
    st.markdown("---")
    col_btn = st.columns([1, 2, 1])[1]
    
    with col_btn:
        generate_button = st.button("🎙 Generate Audiobook", use_container_width=True)
    
    # PROCESS
    if generate_button:
        if not input_text or input_text.strip() == "":
            st.error("❌ Please provide text!")
        else:
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # Step 1
                status_text.text("🔄 Step 1/3: Rewriting...")
                progress_bar.progress(33)
                
                # GET REWRITTEN TEXT
                rewritten_text = rewrite_text_simple(input_text, tone, model, tokenizer)
                
                # DISPLAY IT IMMEDIATELY
                rewritten_display.markdown(f"""
                <div style="background: white; padding: 20px; border-radius: 10px; min-height: 300px; color: black;">
                    <h4 style="color: #333;">📝 {tone} Tone:</h4>
                    <p style="color: #555; line-height: 1.6;">{rewritten_text}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Step 2
                status_text.text(f"🔊 Step 2/3: TTS ({voice})...")
                progress_bar.progress(66)
                
                audio_file = text_to_speech_gtts(rewritten_text, voice)
                
                # Step 3
                status_text.text("✅ Complete!")
                progress_bar.progress(100)
                time.sleep(0.3)
                
                progress_bar.empty()
                status_text.empty()
                
                st.success("🎉 Done!")
                
                # Audio
                st.markdown("---")
                st.markdown(f"### 🎧 Audiobook ({voice})")
                
                col_a1, col_a2 = st.columns([2, 1])
                
                with col_a1:
                    if audio_file:
                        with open(audio_file, 'rb') as audio:
                            st.audio(audio.read(), format='audio/mp3')
                
                with col_a2:
                    if audio_file:
                        with open(audio_file, 'rb') as audio:
                            st.download_button(
                                "📥 Download",
                                audio.read(),
                                f"echoverse_{tone.lower()}.mp3",
                                "audio/mp3",
                                use_container_width=True
                            )
                
                # Comparison
                st.markdown("---")
                st.markdown("### 📊 Side by Side")
                
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("#### Original")
                    st.text_area("", value=input_text, height=150, disabled=True, key="orig")
                with c2:
                    st.markdown(f"#### {tone}")
                    st.text_area("", value=rewritten_text, height=150, disabled=True, key="rw")
                
                # Stats
                st.markdown("---")
                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    st.metric("Original", len(input_text.split()), "words")
                with c2:
                    st.metric("Rewritten", len(rewritten_text.split()), "words")
                with c3:
                    st.metric("Tone", tone)
                with c4:
                    st.metric("Voice", voice.split()[0])
                
            except Exception as e:
                st.error(f"❌ {str(e)}")
                progress_bar.empty()


if _name_ == "_main_":
    main()