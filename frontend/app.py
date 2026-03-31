import os
import requests
import re
import streamlit as st
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# -----------------------------------------------------------------------------
load_dotenv()
API_BASE_URL = os.getenv("FAST_API_URL", "http://backend:8000")

st.set_page_config(
    page_title="Medify AI",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. ADAPTIVE PREMIUM CSS STYLING (Works in Light & Dark Mode)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    /* Hide Streamlit default headers and footers to look like a real app */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Typography adjustments */
    .stApp {
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* Premium Button Styling - Theme Agnostic */
    .stButton > button {
        background-color: #0f766e !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 6px -1px rgba(15, 118, 110, 0.2) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #0d9488 !important;
        box-shadow: 0 8px 12px -1px rgba(15, 118, 110, 0.3) !important;
        transform: translateY(-2px) !important;
        color: #ffffff !important;
    }

    /* Metric Styling (For high visibility outputs) */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 800 !important;
        color: #0f766e !important; /* Teal stands out in both light/dark */
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* Pill Tags for Medical Entities - Adaptive for dark/light */
    .entity-pill {
        display: inline-block;
        background-color: rgba(14, 165, 233, 0.15); /* Transparent blue */
        color: #0ea5e9; /* Bright blue, readable on dark and light */
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 4px;
        border: 1px solid rgba(14, 165, 233, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

def render_pill(text):
    return f'<span class="entity-pill">{text}</span>'

# -----------------------------------------------------------------------------
# 3. API CLIENT FUNCTIONS
# -----------------------------------------------------------------------------
def ocr_extract(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    res = requests.post(f"{API_BASE_URL}/ocr/extract", files=files)
    res.raise_for_status()
    return res.json()

def ner_parse(text: str):
    res = requests.post(f"{API_BASE_URL}/ner/parse", json={"text": text})
    res.raise_for_status()
    return res.json()

def predict_disease(symptoms: list):
    res = requests.post(f"{API_BASE_URL}/prediction/", json={"symptoms": symptoms})
    res.raise_for_status()
    return res.json()

def get_interactions(meds: list):
    res = requests.post(f"{API_BASE_URL}/ai/interactions", json={"medicines": meds})
    res.raise_for_status()
    return res.json()

def verify_prescription(symptom, med_name, age_months, dosage_mg_kg):
    params = {"symptom": symptom, "medicine_name": med_name, "age_in_months": age_months, "given_dosage_mg_per_kg": dosage_mg_kg}
    res = requests.get(f"{API_BASE_URL}/drug_info/verify", params=params)
    res.raise_for_status()
    return res.json()

def get_dosage(med_name, age_months):
    res = requests.get(f"{API_BASE_URL}/drug_info/dosage/{med_name}/{age_months}")
    res.raise_for_status()
    return res.json()

def get_alternatives(med_name):
    res = requests.get(f"{API_BASE_URL}/alternatives/{med_name}")
    if res.status_code == 404: return None
    res.raise_for_status()
    return res.json()

def generate_summary(outputs_list: list):
    res = requests.post(f"{API_BASE_URL}/ai/summarize", json={"outputs": outputs_list})
    res.raise_for_status()
    return res.json()

# -----------------------------------------------------------------------------
# 4. SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if 'app_data' not in st.session_state:
    st.session_state.app_data = {
        'extracted_text': '', 'ner_results': {}, 'prediction_results': [],
        'interaction_results': '', 'verify_results': {}, 'dosage_results': {}, 'alt_results': {}
    }

if 'patient_profile' not in st.session_state:
    st.session_state.patient_profile = {'age_years': 5, 'weight_kg': 20.0}

# -----------------------------------------------------------------------------
# 5. SIDEBAR NAVIGATION & GLOBAL PROFILE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #0f766e;'>⚕️ Medify</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-weight:600;'>Intelligent Medical Assistant</p>", unsafe_allow_html=True)
    st.write("---")
    
    menu = st.radio(
        "Navigation Menu",
        [
            "🏠 Dashboard Overview", 
            "1️⃣ OCR & Extraction", 
            "2️⃣ Disease Prediction", 
            "3️⃣ Drug Interactions", 
            "4️⃣ Verification & Dosage", 
            "5️⃣ Cost & Alternatives", 
            "6️⃣ AI Final Summary"
        ],
        label_visibility="collapsed",
        key="main_navigation_radio"
    )
    
    st.write("---")
    
    st.markdown("### 👤 Patient Profile")
    new_age = st.number_input("Age (Years)", min_value=0, max_value=120, value=st.session_state.patient_profile['age_years'], step=1, key="global_sidebar_age")
    new_weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=st.session_state.patient_profile['weight_kg'], step=0.5, key="global_sidebar_weight")
    
    st.session_state.patient_profile['age_years'] = new_age
    st.session_state.patient_profile['weight_kg'] = new_weight

# -----------------------------------------------------------------------------
# 6. VIEW RENDERERS (DASHBOARD PAGES)
# -----------------------------------------------------------------------------

if menu == "🏠 Dashboard Overview":
    st.title("⚕️ Welcome to Medify")
    st.markdown("Your AI-powered prescription companion. Select a step from the sidebar to begin processing.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### 📄 Extraction")
            st.write("Upload prescriptions to instantly digitize and identify medications and symptoms.")
    with col2:
        with st.container(border=True):
            st.markdown("### 🛡️ Safety")
            st.write("Automatically verify prescribed dosages against standard pediatric & adult guidelines.")
    with col3:
        with st.container(border=True):
            st.markdown("### 🤖 Intelligence")
            st.write("Predict diseases, flag drug interactions, and discover cost-saving generic alternatives.")

elif menu == "1️⃣ OCR & Extraction":
    st.title("📄 1. Prescription Digitization")
    st.markdown("Upload a prescription image to automatically extract text and identify medical entities.")
    
    col_in, col_out = st.columns([1, 1], gap="large")
    
    with col_in:
        with st.container(border=True):
            st.markdown("#### 📥 Input Source")
            tab1, tab2, tab3 = st.tabs(["Upload Image", "Camera", "Manual Text"])
            
            with tab1:
                img_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"], key="upload_img")
                if img_file and st.button("Extract Text", key="btn_extract_upload"):
                    with st.spinner("Processing via GCP Vision..."):
                        try:
                            res = ocr_extract(img_file)
                            st.session_state.app_data['extracted_text'] = res.get("extracted_text", "")
                            st.success("Text extracted successfully!")
                        except Exception as e: st.error(f"OCR Error: {e}")
                            
            with tab2:
                cam_file = st.camera_input("Take a photo", key="cam_img")
                if cam_file and st.button("Extract Text", key="btn_extract_cam"):
                    with st.spinner("Processing..."):
                        try:
                            res = ocr_extract(cam_file)
                            st.session_state.app_data['extracted_text'] = res.get("extracted_text", "")
                            st.success("Text extracted successfully!")
                        except Exception as e: st.error(f"OCR Error: {e}")
                            
            with tab3:
                manual_txt = st.text_area("Paste text here:", value=st.session_state.app_data['extracted_text'], height=150, key="txt_manual")
                if st.button("Save Text", key="btn_extract_manual"):
                    st.session_state.app_data['extracted_text'] = manual_txt
                    st.success("Text saved!")

    with col_out:
        with st.container(border=True):
            st.markdown("#### 🧠 Extracted Entities")
            if st.session_state.app_data['extracted_text']:
                if st.button("Run AI Recognition", key="btn_run_ner"):
                    with st.spinner("Identifying medical terms..."):
                        try:
                            ner_res = ner_parse(st.session_state.app_data['extracted_text'])
                            st.session_state.app_data['ner_results'] = ner_res.get("entities", {})
                        except Exception as e: st.error(f"NER Error: {e}")
                
                entities = st.session_state.app_data['ner_results']
                if entities:
                    st.markdown("**💊 Medications:**")
                    meds = entities.get("Medication", [])
                    st.markdown(" ".join([render_pill(m) for m in meds]) if meds else "*None*", unsafe_allow_html=True)
                    
                    st.markdown("<br>**🤒 Symptoms:**", unsafe_allow_html=True)
                    symps = entities.get("Symptoms", [])
                    st.markdown(" ".join([render_pill(s) for s in symps]) if symps else "*None*", unsafe_allow_html=True)
                    
                    st.markdown("<br>**⚖️ Dosages:**", unsafe_allow_html=True)
                    for d in entities.get("Dosage", []): st.markdown(f"- {d}")
            else:
                st.info("Upload an image on the left to begin.")

elif menu == "2️⃣ Disease Prediction":
    st.title("🩺 2. AI Disease Prediction")
    st.markdown("Predict potential diseases based on patient symptoms.")
    
    ner_symps = st.session_state.app_data['ner_results'].get('Symptoms', [])
    default_symps = ", ".join(ner_symps)
    
    with st.container(border=True):
        symps_input = st.text_input("Symptoms (comma-separated):", value=default_symps, key="pred_input")
        if st.button("Analyze Symptoms", key="btn_predict"):
            symp_list = [s.strip() for s in symps_input.split(",") if s.strip()]
            if not symp_list:
                st.warning("Please enter at least one symptom.")
            else:
                with st.spinner("Analyzing..."):
                    try:
                        preds = predict_disease(symp_list).get("predictions", [])
                        st.session_state.app_data['prediction_results'] = preds
                        if preds:
                            for p in preds:
                                prob_float = float(p['probability'].strip('%')) / 100
                                st.markdown(f"### {p['disease'].title().replace('_', ' ')}")
                                c1, c2 = st.columns([0.8, 0.2])
                                c1.progress(prob_float)
                                c2.markdown(f"<h3 style='margin:0; color:#0f766e;'>{p['probability']}</h3>", unsafe_allow_html=True)
                                st.write("---")
                        else: st.info("No strong predictions found.")
                    except Exception as e: st.error(f"Error: {e}")

elif menu == "3️⃣ Drug Interactions":
    st.title("⚡ 3. Drug Interaction Check")
    st.markdown("Check for adverse interactions between prescribed medications.")
    
    ner_meds = st.session_state.app_data['ner_results'].get('Medication', [])
    meds_input = st.text_area("Medications (comma-separated):", value=", ".join(ner_meds), key="int_input")
    
    if st.button("Analyze Interactions", key="btn_interactions"):
        med_list = [m.strip() for m in meds_input.split(",") if m.strip()]
        if len(med_list) < 2:
            st.warning("Please enter at least 2 medications.")
        else:
            with st.spinner("Checking pharmacological data..."):
                try:
                    res = get_interactions(med_list)
                    st.session_state.app_data['interaction_results'] = res
                    with st.container(border=True): st.markdown(res)
                except Exception as e: st.error(f"Error: {e}")

elif menu == "4️⃣ Verification & Dosage":
    st.title("✅ 4. Safety Verification")
    
    age_months = st.session_state.patient_profile['age_years'] * 12
    weight = st.session_state.patient_profile['weight_kg']
    st.info(f"**Patient Profile:** {st.session_state.patient_profile['age_years']} Years Old | {weight} kg")
    
    ner = st.session_state.app_data['ner_results']
    d_med = ner.get('Medication', [""])[0] if ner.get('Medication') else ""
    d_symp = ner.get('Symptoms', [""])[0] if ner.get('Symptoms') else ""
    d_dose = ner.get('Dosage', [""])[0] if ner.get('Dosage') else ""

    tab1, tab2 = st.tabs(["Safety Check", "Guidelines Lookup"])
    
    with tab1:
        with st.container(border=True):
            c1, c2, c3 = st.columns(3)
            with c1: v_med = st.text_input("Medication", value=d_med, key="v_med")
            with c2: v_symp = st.text_input("Symptom", value=d_symp, key="v_symp")
            with c3: v_dose = st.text_input("Dose (e.g. '500 mg')", value=d_dose, key="v_dose")
                
            if st.button("Verify Safety", key="btn_verify"):
                if not (v_med and v_symp and v_dose): st.warning("Fill all fields.")
                else:
                    try:
                        match = re.search(r'(\d+\.?\d*)', v_dose)
                        if not match: raise ValueError("No numeric dose found.")
                        dose_mg_kg = float(match.group(1)) / weight
                        
                        with st.spinner("Verifying..."):
                            report = verify_prescription(v_symp, v_med, age_months, dose_mg_kg)
                            st.session_state.app_data['verify_results'] = report
                            
                            st.markdown(f"**Calculated Administered Dose:** `{dose_mg_kg:.2f} mg/kg`")
                            r1, r2, r3 = st.columns(3)
                            
                            def fmt(val): return "✅ Safe" if "pass" in val.lower() else ("➖ N/A" if "not applicable" in val.lower() else "⚠️ Warning")
                            
                            r1.metric("Symptom Check", fmt(report.get("symptom_check", "")), help=report.get("symptom_check"))
                            r2.metric("Age Check", fmt(report.get("age_check", "")), help=report.get("age_check"))
                            r3.metric("Dosage Check", fmt(report.get("dosage_check", "")), help=report.get("dosage_check"))
                            
                            if report.get("notes"):
                                st.markdown("#### Notes:")
                                for n in report.get("notes", []): st.markdown(f"- {n}")
                    except Exception as e: st.error(f"Error: {e}")

    with tab2:
        with st.container(border=True):
            guideline_med = st.text_input("Search Medication", value=d_med, key="guide_med")
            if st.button("Fetch Guidelines", key="btn_guide"):
                with st.spinner("Fetching..."):
                    try:
                        res = get_dosage(guideline_med, age_months)
                        st.markdown(f"### 💊 Guidelines for {res.get('drug_generic', guideline_med)}")
                        g1, g2 = st.columns(2)
                        g1.metric("Max Daily Dose", f"{res.get('max_daily_dose')} {res.get('max_daily_dose_units')}")
                        g2.metric("Dosing Interval", f"Every {res.get('dosing_interval_hours')} hours")
                        st.warning(f"**Safety Flag:** {res.get('notes_key_safety', 'None listed.')}")
                    except Exception as e: st.error(f"Error: {e}")

elif menu == "5️⃣ Cost & Alternatives":
    st.title("💸 5. Alternatives & Cost Comparison")
    
    d_med = st.session_state.app_data['ner_results'].get('Medication', [""])[0] if st.session_state.app_data['ner_results'].get('Medication') else ""
    alt_med = st.text_input("Medication Name", value=d_med, key="alt_med_input")
    
    if st.button("Search Database", key="btn_alt"):
        with st.spinner("Searching..."):
            try:
                res = get_alternatives(alt_med)
                if not res: st.warning("No data found.")
                else:
                    st.session_state.app_data['alt_results'] = res
                    with st.container(border=True):
                        st.markdown(f"## {alt_med.title()}")
                        st.caption(res.get('description', ''))
                        st.metric("Base Price", f"₹{res.get('price_in_inr', 0)}")
                        st.write("---")
                        
                        ca, cb = st.columns(2)
                        with ca:
                            st.markdown("#### 💊 Cheaper Alternatives")
                            for alt in res.get('alternatives', []):
                                with st.expander(f"**{alt['name']}**"):
                                    c1, c2 = st.columns(2)
                                    c1.metric("Price", f"₹{alt['price_in_inr']}")
                                    c2.metric("Savings", f"{alt['savings_percentage']}%")
                        with cb:
                            st.markdown("#### 🌿 Home Remedies")
                            for cond, rem in res.get('home_remedies_for_common_uses', {}).items():
                                st.markdown(f"- **{cond}:** {rem}")
            except Exception as e: st.error(f"Error: {e}")

elif menu == "6️⃣ AI Final Summary":
    st.title("🤖 6. AI Patient Summary")
    st.markdown("Synthesize all gathered data into a single clinical report.")
    
    with st.container(border=True):
        st.markdown("#### Data Collection Status")
        flags = {
            "OCR/NER": bool(st.session_state.app_data['ner_results']),
            "Verification": bool(st.session_state.app_data['verify_results']),
            "Interactions": bool(st.session_state.app_data['interaction_results']),
            "Alternatives": bool(st.session_state.app_data['alt_results'])
        }
        
        cols = st.columns(4)
        for i, (k, v) in enumerate(flags.items()):
            # Fixed: Standard if/else prevents Streamlit 'Magic' from printing raw objects
            if v:
                cols[i].success(f"✅ {k}")
            else:
                cols[i].error(f"❌ {k}")
                
        if st.button("Generate AI Report", key="btn_summary"):
            outputs = [{k: v} for k, v in st.session_state.app_data.items() if v and k != "extracted_text"]
            if not outputs: 
                st.warning("No data available.")
            else:
                with st.spinner("Crafting summary..."):
                    try:
                        summary = generate_summary(outputs)
                        st.write("---")
                        st.markdown("### 📋 Final Analysis Report")
                        st.markdown(summary)
                    except Exception as e: 
                        st.error(f"Error: {e}")
