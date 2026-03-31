import os
import requests
import re
import streamlit as st
from dotenv import load_dotenv
import time

# -----------------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# -----------------------------------------------------------------------------
load_dotenv()
API_BASE_URL = os.getenv("FAST_API_URL", "http://backend:8000")

st.set_page_config(
    page_title="Medify AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. THEME-ADAPTIVE VIBRANT CSS STYLING
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* Hide Streamlit Clutter */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Vibrant Gradient Headers (Works on Dark & Light Mode) */
    .gradient-text {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 0.5rem;
    }
    .sub-gradient-text {
        background: linear-gradient(135deg, #ec4899 0%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }

    /* Premium Button Styling (Gradient) */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.2rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.5) !important;
    }

    /* Output Containers / Cards - NO BACKGROUND COLOR (Let Streamlit handle it) */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border-radius: 16px;
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(149, 157, 165, 0.15);
    }

    /* Metric Styling (Vibrant Purple for both modes) */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: #8b5cf6 !important;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1.1rem !important;
        font-weight: 700 !important;
    }

    /* Dynamic Colorful Pill Tags (Transparent backgrounds for dark mode compatibility) */
    .pill {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 9999px;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 4px;
        border: 1px solid;
    }
    .pill-medication { background: rgba(139, 92, 246, 0.15); color: #a78bfa; border-color: rgba(139, 92, 246, 0.3); }
    .pill-symptom { background: rgba(244, 63, 94, 0.15); color: #fb7185; border-color: rgba(244, 63, 94, 0.3); }
    .pill-dosage { background: rgba(16, 185, 129, 0.15); color: #34d399; border-color: rgba(16, 185, 129, 0.3); }
    .pill-freq { background: rgba(14, 165, 233, 0.15); color: #38bdf8; border-color: rgba(14, 165, 233, 0.3); }

    /* Light mode text colors for pills (using media query) */
    @media (prefers-color-scheme: light) {
        .pill-medication { color: #7c3aed; }
        .pill-symptom { color: #e11d48; }
        .pill-dosage { color: #059669; }
        .pill-freq { color: #0284c7; }
    }
    </style>
""", unsafe_allow_html=True)


def render_pill(text, category="medication"):
    return f'<span class="pill pill-{category}">{text}</span>'

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

# Helper function to load demo scenarios
def load_scenario(text, age, weight):
    with st.spinner("🚀 Running AI Extraction Engine..."):
        st.session_state.patient_profile['age_years'] = age
        st.session_state.patient_profile['weight_kg'] = weight
        st.session_state.app_data['extracted_text'] = text
        try:
            ner_res = ner_parse(text)
            st.session_state.app_data['ner_results'] = ner_res.get("entities", {})
            time.sleep(1) # Just to let the user see the spinner
        except Exception as e:
            st.error(f"Failed to load demo: {e}")

# -----------------------------------------------------------------------------
# 5. SIDEBAR NAVIGATION & GLOBAL PROFILE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'><span class='gradient-text' style='font-size:2.5rem;'>Medify ✨</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.7; font-weight:600;'>Intelligent Medical Assistant</p>", unsafe_allow_html=True)
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
    new_weight = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=float(st.session_state.patient_profile['weight_kg']), step=0.5, key="global_sidebar_weight")
    
    st.session_state.patient_profile['age_years'] = new_age
    st.session_state.patient_profile['weight_kg'] = new_weight

# -----------------------------------------------------------------------------
# 6. VIEW RENDERERS (DASHBOARD PAGES)
# -----------------------------------------------------------------------------

if menu == "🏠 Dashboard Overview":
    st.markdown("<div class='gradient-text'>Welcome to Medify.</div>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.2rem; opacity: 0.8;'>Your next-generation AI companion for safe, smart, and cost-effective healthcare decisions.</p>", unsafe_allow_html=True)
    
    # Feature Highlights
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### 📄 Smart Digitization")
            st.write("Turn messy physical prescriptions into structured digital data using AI-driven Optical Character Recognition.")
    with col2:
        with st.container(border=True):
            st.markdown("### 🛡️ Safety Engine")
            st.write("Instantly flag life-threatening drug interactions and age/weight-based dosage errors before they happen.")
    with col3:
        with st.container(border=True):
            st.markdown("### 💸 Cost Optimizer")
            st.write("Discover highly-rated generic alternatives and traditional home remedies to drastically lower healthcare costs.")

    st.write("---")
    
    # Interactive Demos Section
    st.markdown("### ⚡ Try a Live Scenario")
    st.markdown("Click a scenario below to instantly load mock patient data and extract the medical entities using our AI.")
    
    d1, d2, d3 = st.columns(3)
    
    with d1:
        with st.container(border=True):
            st.markdown("#### 👶 Pediatric Fever")
            st.caption("Patient: 5 Yrs, 20kg")
            st.markdown("<p style='opacity:0.7; font-style:italic;'>\"Rx: Paracetamol 250mg, 5ml twice a day. Advised for fever and body ache.\"</p>", unsafe_allow_html=True)
            if st.button("Test This Scenario", key="demo_ped"):
                load_scenario("Rx: Paracetamol 250mg, 5ml twice a day. Advised for fever and body ache.", 5, 20.0)
                st.success("Loaded! Check 'Extracted Data' below or go to Step 4.")
                
    with d2:
        with st.container(border=True):
            st.markdown("#### 👴 Adult Chronic")
            st.caption("Patient: 60 Yrs, 75kg")
            st.markdown("<p style='opacity:0.7; font-style:italic;'>\"Metformin 500mg daily. Amlodipine 5mg once a day. For diabetes and high blood pressure.\"</p>", unsafe_allow_html=True)
            if st.button("Test This Scenario", key="demo_adult"):
                load_scenario("Metformin 500mg daily. Amlodipine 5mg once a day. For diabetes and high blood pressure.", 60, 75.0)
                st.success("Loaded! Go to Step 3 to check drug interactions.")

    with d3:
        with st.container(border=True):
            st.markdown("#### 🤒 Severe Infection")
            st.caption("Patient: 30 Yrs, 65kg")
            st.markdown("<p style='opacity:0.7; font-style:italic;'>\"Azithromycin 500mg stat. Cetirizine 10mg at bedtime. For severe cold and cough.\"</p>", unsafe_allow_html=True)
            if st.button("Test This Scenario", key="demo_inf"):
                load_scenario("Azithromycin 500mg stat. Cetirizine 10mg at bedtime. For severe cold and cough.", 30, 65.0)
                st.success("Loaded! Go to Step 2 to predict the exact disease.")

    # Show active data if exists
    if st.session_state.app_data.get('ner_results'):
        st.write("---")
        st.markdown("### 🧠 Currently Active Extracted Data")
        entities = st.session_state.app_data['ner_results']
        
        c_med, c_sym = st.columns(2)
        with c_med:
            st.markdown("**💊 Medications**")
            st.markdown(" ".join([render_pill(m, "medication") for m in entities.get("Medication", [])]) or "*None*", unsafe_allow_html=True)
        with c_sym:
            st.markdown("**🤒 Symptoms**")
            st.markdown(" ".join([render_pill(s, "symptom") for s in entities.get("Symptoms", [])]) or "*None*", unsafe_allow_html=True)

elif menu == "1️⃣ OCR & Extraction":
    st.markdown("<h1 class='gradient-text'>📄 Digitization Hub</h1>", unsafe_allow_html=True)
    st.markdown("Upload a prescription to automatically extract text and identify medical entities.")
    
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
            st.markdown("#### 🧠 AI Entity Recognition")
            if st.session_state.app_data['extracted_text']:
                if st.button("Run AI Recognition", key="btn_run_ner"):
                    with st.spinner("Identifying medical terms..."):
                        try:
                            ner_res = ner_parse(st.session_state.app_data['extracted_text'])
                            st.session_state.app_data['ner_results'] = ner_res.get("entities", {})
                        except Exception as e: st.error(f"NER Error: {e}")
                
                entities = st.session_state.app_data['ner_results']
                if entities:
                    st.write("") # spacing
                    st.markdown("**💊 Medications**")
                    st.markdown(" ".join([render_pill(m, "medication") for m in entities.get("Medication", [])]) or "*None*", unsafe_allow_html=True)
                    
                    st.markdown("<br>**🤒 Symptoms**", unsafe_allow_html=True)
                    st.markdown(" ".join([render_pill(s, "symptom") for s in entities.get("Symptoms", [])]) or "*None*", unsafe_allow_html=True)
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("<br>**⚖️ Dosages**", unsafe_allow_html=True)
                        st.markdown(" ".join([render_pill(d, "dosage") for d in entities.get("Dosage", [])]) or "*None*", unsafe_allow_html=True)
                    with c2:
                        st.markdown("<br>**⏱️ Frequencies**", unsafe_allow_html=True)
                        st.markdown(" ".join([render_pill(f, "freq") for f in entities.get("Frequency", [])]) or "*None*", unsafe_allow_html=True)
            else:
                st.info("Upload an image or enter text on the left to begin.")

elif menu == "2️⃣ Disease Prediction":
    st.markdown("<h1 class='gradient-text'>🩺 Disease Predictor</h1>", unsafe_allow_html=True)
    st.markdown("Powered by Machine Learning to predict potential diseases based on patient symptoms.")
    
    ner_symps = st.session_state.app_data['ner_results'].get('Symptoms', [])
    default_symps = ", ".join(ner_symps)
    
    with st.container(border=True):
        symps_input = st.text_input("Symptoms (comma-separated):", value=default_symps, key="pred_input")
        if st.button("Analyze Symptoms", key="btn_predict"):
            symp_list = [s.strip() for s in symps_input.split(",") if s.strip()]
            if not symp_list:
                st.warning("Please enter at least one symptom.")
            else:
                with st.spinner("Running prediction model..."):
                    try:
                        preds = predict_disease(symp_list).get("predictions", [])
                        st.session_state.app_data['prediction_results'] = preds
                        if preds:
                            st.markdown("### 📊 Top Predictions")
                            for p in preds:
                                prob_float = float(p['probability'].strip('%')) / 100
                                st.markdown(f"**{p['disease'].title().replace('_', ' ')}**")
                                c1, c2 = st.columns([0.85, 0.15])
                                c1.progress(prob_float)
                                c2.markdown(f"<span class='sub-gradient-text' style='font-size:1.4rem;'>{p['probability']}</span>", unsafe_allow_html=True)
                                st.write("---")
                        else: st.info("No strong predictions found.")
                    except Exception as e: st.error(f"Error: {e}")

elif menu == "3️⃣ Drug Interactions":
    st.markdown("<h1 class='gradient-text'>⚡ Interaction Checker</h1>", unsafe_allow_html=True)
    st.markdown("Check for adverse interactions between prescribed medications using Generative AI.")
    
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
    st.markdown("<h1 class='gradient-text'>✅ Safety Verification</h1>", unsafe_allow_html=True)
    
    age_months = st.session_state.patient_profile['age_years'] * 12
    weight = st.session_state.patient_profile['weight_kg']
    st.info(f"👤 **Patient Profile Selected:** {st.session_state.patient_profile['age_years']} Years Old | {weight} kg")
    
    ner = st.session_state.app_data['ner_results']
    d_med = ner.get('Medication', [""])[0] if ner.get('Medication') else ""
    d_symp = ner.get('Symptoms', [""])[0] if ner.get('Symptoms') else ""
    d_dose = ner.get('Dosage', [""])[0] if ner.get('Dosage') else ""

    tab1, tab2 = st.tabs(["🛡️ Safety Check", "📋 Guidelines Lookup"])
    
    with tab1:
        with st.container(border=True):
            c1, c2, c3 = st.columns(3)
            with c1: v_med = st.text_input("Medication", value=d_med, key="v_med")
            with c2: v_symp = st.text_input("Symptom", value=d_symp, key="v_symp")
            with c3: v_dose = st.text_input("Dose (e.g. '500 mg')", value=d_dose, key="v_dose")
                
            if st.button("Verify Safety Engine", key="btn_verify"):
                if not (v_med and v_symp and v_dose): st.warning("Fill all fields.")
                else:
                    try:
                        match = re.search(r'(\d+\.?\d*)', v_dose)
                        if not match: raise ValueError("No numeric dose found.")
                        dose_mg_kg = float(match.group(1)) / weight
                        
                        with st.spinner("Cross-referencing datasets..."):
                            report = verify_prescription(v_symp, v_med, age_months, dose_mg_kg)
                            st.session_state.app_data['verify_results'] = report
                            
                            st.markdown(f"<p style='font-size:1.1rem;'><b>Calculated Administered Dose:</b> <span style='color:#ec4899;'>{dose_mg_kg:.2f} mg/kg</span></p>", unsafe_allow_html=True)
                            r1, r2, r3 = st.columns(3)
                            
                            def fmt(val): return "✅ Safe" if "pass" in val.lower() else ("➖ N/A" if "not applicable" in val.lower() else "⚠️ Warning")
                            
                            r1.metric("Symptom Check", fmt(report.get("symptom_check", "")), help=report.get("symptom_check"))
                            r2.metric("Age Check", fmt(report.get("age_check", "")), help=report.get("age_check"))
                            r3.metric("Dosage Check", fmt(report.get("dosage_check", "")), help=report.get("dosage_check"))
                            
                            if report.get("notes"):
                                st.markdown("#### Important Notes:")
                                for n in report.get("notes", []): st.markdown(f"- {n}")
                    except Exception as e: st.error(f"Error: {e}")

    with tab2:
        with st.container(border=True):
            guideline_med = st.text_input("Search Medication Database", value=d_med, key="guide_med")
            if st.button("Fetch Standard Guidelines", key="btn_guide"):
                with st.spinner("Fetching..."):
                    try:
                        res = get_dosage(guideline_med, age_months)
                        st.markdown(f"### 💊 Guidelines for {res.get('drug_generic', guideline_med).title()}")
                        g1, g2 = st.columns(2)
                        g1.metric("Max Daily Dose", f"{res.get('max_daily_dose')} {res.get('max_daily_dose_units')}")
                        g2.metric("Dosing Interval", f"Every {res.get('dosing_interval_hours')} hours")
                        st.warning(f"**Safety Flag:** {res.get('notes_key_safety', 'None listed.')}")
                    except Exception as e: st.error(f"Error: {e}")

elif menu == "5️⃣ Cost & Alternatives":
    st.markdown("<h1 class='gradient-text'>💸 Cost Optimizer</h1>", unsafe_allow_html=True)
    st.markdown("Find generic alternatives to save money, and view established natural remedies.")
    
    d_med = st.session_state.app_data['ner_results'].get('Medication', [""])[0] if st.session_state.app_data['ner_results'].get('Medication') else ""
    alt_med = st.text_input("Medication Name", value=d_med, key="alt_med_input")
    
    if st.button("Search Market Data", key="btn_alt"):
        with st.spinner("Searching database..."):
            try:
                res = get_alternatives(alt_med)
                if not res: st.warning("No data found in market database.")
                else:
                    st.session_state.app_data['alt_results'] = res
                    with st.container(border=True):
                        st.markdown(f"## {alt_med.title()}")
                        st.caption(res.get('description', ''))
                        st.markdown(f"### <span class='sub-gradient-text'>Base Price: ₹{res.get('price_in_inr', 0)}</span>", unsafe_allow_html=True)
                        st.write("---")
                        
                        ca, cb = st.columns(2)
                        with ca:
                            st.markdown("#### 💊 Cheaper Generic Alternatives")
                            for alt in res.get('alternatives', []):
                                with st.expander(f"**{alt['name']}**"):
                                    c1, c2 = st.columns(2)
                                    c1.metric("Price", f"₹{alt['price_in_inr']}")
                                    c2.metric("Savings", f"{alt['savings_percentage']}%")
                        with cb:
                            st.markdown("#### 🌿 Traditional Remedies")
                            for cond, rem in res.get('home_remedies_for_common_uses', {}).items():
                                st.markdown(f"- **{cond}:** {rem}")
            except Exception as e: st.error(f"Error: {e}")

elif menu == "6️⃣ AI Final Summary":
    st.markdown("<h1 class='gradient-text'>🤖 AI Clinical Report</h1>", unsafe_allow_html=True)
    st.markdown("Synthesize all gathered insights into a single clinical summary.")
    
    with st.container(border=True):
        st.markdown("#### 📊 Data Collection Pipeline Status")
        flags = {
            "Entity Extraction": bool(st.session_state.app_data['ner_results']),
            "Safety Protocol": bool(st.session_state.app_data['verify_results']),
            "Pharmacology": bool(st.session_state.app_data['interaction_results']),
            "Market Economics": bool(st.session_state.app_data['alt_results'])
        }
        
        cols = st.columns(4)
        for i, (k, v) in enumerate(flags.items()):
            if v:
                cols[i].success(f"✅ {k}")
            else:
                cols[i].error(f"❌ {k}")
                
        st.write("---")
                
        if st.button("Generate Executive Summary", key="btn_summary"):
            outputs = [{k: v} for k, v in st.session_state.app_data.items() if v and k != "extracted_text"]
            if not outputs: 
                st.warning("No data available in the pipeline. Please run previous steps.")
            else:
                with st.spinner("Crafting comprehensive report..."):
                    try:
                        summary = generate_summary(outputs)
                        st.markdown("### 📋 Final Analysis Report")
                        st.markdown(summary)
                    except Exception as e: st.error(f"Error: {e}")
