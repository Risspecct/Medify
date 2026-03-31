import streamlit as st
from api import generate_summary

def render():
    st.title("🤖 Step 6: Final AI Report")
    st.markdown("Synthesize all the gathered analysis into a single, comprehensive patient summary.")
    
    # Show status of collected data
    st.markdown("#### Data Collection Status")
    flags = {
        "OCR/NER Extraction": bool(st.session_state.app_data.get('ner_results')),
        "Safety Verification": bool(st.session_state.app_data.get('verify_results')),
        "Drug Interactions": bool(st.session_state.app_data.get('interaction_results')),
        "Cost & Alternatives": bool(st.session_state.app_data.get('alt_results'))
    }
    
    cols = st.columns(4)
    for i, (k, v) in enumerate(flags.items()):
        if v:
            cols[i].success(f"✅ {k}")
        else:
            cols[i].error(f"❌ {k}")
            
    st.write("---")
    
    if st.button("Generate Final Report", type="primary", use_container_width=True):
        outputs_to_send = []
        for k, v in st.session_state.app_data.items():
            if v and k != "extracted_text": # Send all structured JSON data
                outputs_to_send.append({k: v})
                
        if not outputs_to_send:
            st.warning("No data available to summarize. Please run the other steps first.")
        else:
            with st.spinner("Gemini AI is crafting the final clinical summary..."):
                try:
                    summary = generate_summary(outputs_to_send)
                    with st.container(border=True):
                        st.markdown("### 📋 Final Analysis Report")
                        st.markdown(summary)
                except Exception as e:
                    st.error(f"Summarizer Error: {e}")
