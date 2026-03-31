import os
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()
API_BASE_URL = os.getenv("FAST_API_URL", "http://backend:8000")

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION & THEME
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Medify Dashboard",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for sleek look
st.markdown("""
    <style>
    .stButton > button { border-radius: 8px; font-weight: bold; }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .css-1d391kg { padding-top: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if 'shared_data' not in st.session_state:
    st.session_state.shared_data = {
        'extracted_text': '',
        'ner_results': {},
        'verify_results': {},
        'dosage_results': {},
        'interaction_results': '',
        'prediction_results': [],
        'alt_results': {}
    }

# -----------------------------------------------------------------------------
# API HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def api_post_ocr(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    res = requests.post(f"{API_BASE_URL}/ocr/extract", files=files)
    res.raise_for_status()
    return res.json()

def api_post_ner(text):
    res = requests.post(f"{API_BASE_URL}/ner/parse", json={"text": text})
    res.raise_for_status()
    return res.json()

def api_post_predict(symptoms):
    res = requests.post(f"{API_BASE_URL}/prediction/", json={"symptoms": symptoms})
    res.raise_for_status()
    return res.json()

def api_post_interactions(meds):
    res = requests.post(f"{API_BASE_URL}/ai/interactions", json={"medicines": meds})
    res.raise_for_status()
    return res.json()

def api_get_verify(symptom, med_name, age_months, dosage_mg_kg):
    params = {
        "symptom": symptom, "medicine_name": med_name, 
        "age_in_months": age_months, "given_dosage_mg_per_kg": dosage_mg_kg
    }
    res = requests.get(f"{API_BASE_URL}/drug_info/verify", params=params)
    res.raise_for_status()
    return res.json()

def api_get_dosage(med_name, age_months):
    res = requests.get(f"{API_BASE_URL}/drug_info/dosage/{med_name}/{age_months}")
    res.raise_for_status()
    return res.json()

def api_get_alternatives(med_name):
    res = requests.get(f"{API_BASE_URL}/alternatives/{med_name}")
    if res.status_code == 404: return None
    res.raise_for_status()
    return res.json()

def api_post_summary(outputs_list):
    res = requests.post(f"{API_BASE_URL}/ai/summarize", json={"outputs": outputs_list})
    res.raise_for_status()
    return res.json()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & GLOBAL PATIENT PROFILE
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=60)
    st.title("Medify")
    st.caption("AI-Powered Prescription Analysis")
    
    st.divider()
    
    st.subheader("📌 Navigation")
    menu = st.radio(
        "Go to",
        ["Dashboard Overview", 
         "1. OCR & Information Extraction", 
         "2. Disease Prediction",
         "3. Drug Interactions", 
         "4. Verification & Dosage", 
         "5. Cost & Alternatives", 
         "6. AI Final Summary"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.subheader("👤 Patient Profile")
    patient_age_yrs = st.number_input("Age (Years)", min_value=0, max_value=120, value=5, step=1)
    patient_weight_kg = st.number_input("Weight (kg)", min_value=1.0, max_value=200.0, value=20.0, step=0.5)
    
    # Auto-calculated context
    patient_age_months = patient_age_yrs * 12

# Helper to get default values from NER
def get_ner_list(key):
    return st.session_state.shared_data['ner_results'].get(key, [])
def get_ner_first(key):
    items = get_ner_list(key)
    return items[0] if items else ""

# -----------------------------------------------------------------------------
# MAIN APP ROUTING
# -----------------------------------------------------------------------------

if menu == "Dashboard Overview":
    st.title("⚕️ Welcome to Medify Dashboard")
    st.markdown("Your intelligent medical assistant. Navigate through the sidebar to process a prescription step-by-step or jump to specific tools.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Smart Extraction**\n\nUpload prescriptions to automatically detect drugs, dosages, and symptoms using OCR & NER.")
    with col2:
        st.warning("**Safety Verification**\n\nCross-check prescribed medications against patient age, weight, and standard dosage rules.")
    with col3:
        st.success("**AI Insights**\n\nPredict diseases, check complex drug interactions, and find cost-effective alternative medicines.")
    
    st.divider()
    if st.session_state.shared_data['ner_results']:
        st.subheader("Current Active Session Data")
        st.json(st.session_state.shared_data['ner_results'])
    else:
        st.markdown("*(No active prescription data. Go to **OCR & Information Extraction** to begin.)*")

elif menu == "1. OCR & Information Extraction":
    st.title("📄 1. Prescription Digitization & NER")
    st.markdown("Upload a prescription image or enter text to extract medical entities.")
    
    col_input, col_output = st.columns([1, 1], gap="large")
    
    with col_input:
        st.subheader("Input Source")
        tabs = st.tabs(["Upload Image", "Camera", "Manual Text"])
        extracted_text = ""
        
        with tabs[0]:
            img_file = st.file_uploader("Upload Prescription", type=["png", "jpg", "jpeg"])
            if img_file and st.button("Extract Text from Image", use_container_width=True):
                with st.spinner("Processing image via GCP Vision..."):
                    try:
                        res = api_post_ocr(img_file)
                        extracted_text = res.get("extracted_text", "")
                        st.session_state.shared_data['extracted_text'] = extracted_text
                        st.success("Extraction Complete!")
                    except Exception as e:
                        st.error(f"OCR Error: {e}")
                        
        with tabs[1]:
            cam_file = st.camera_input("Take a photo")
            if cam_file and st.button("Extract Text from Camera", use_container_width=True):
                with st.spinner("Processing image..."):
                    try:
                        res = api_post_ocr(cam_file)
                        extracted_text = res.get("extracted_text", "")
                        st.session_state.shared_data['extracted_text'] = extracted_text
                        st.success("Extraction Complete!")
                    except Exception as e:
                        st.error(f"OCR Error: {e}")
                        
        with tabs[2]:
            manual_text = st.text_area("Paste text manually:", value=st.session_state.shared_data['extracted_text'], height=150)
            if st.button("Use Text", use_container_width=True):
                extracted_text = manual_text
                st.session_state.shared_data['extracted_text'] = extracted_text
                
        if st.session_state.shared_data['extracted_text']:
            with st.expander("View Raw Text"):
                st.write(st.session_state.shared_data['extracted_text'])

    with col_output:
        st.subheader("Extracted Medical Entities")
        if st.session_state.shared_data['extracted_text']:
            if st.button("Run AI Extraction (NER)", type="primary", use_container_width=True):
                with st.spinner("Parsing medical entities..."):
                    try:
                        ner_res = api_post_ner(st.session_state.shared_data['extracted_text'])
                        st.session_state.shared_data['ner_results'] = ner_res.get("entities", {})
                    except Exception as e:
                        st.error(f"NER Error: {e}")
            
            entities = st.session_state.shared_data['ner_results']
            if entities:
                st.container(border=True)
                c1, c2 = st.columns(2)
                c1.metric("💊 Medications", ", ".join(entities.get("Medication", [])) or "None")
                c2.metric("🤒 Symptoms", ", ".join(entities.get("Symptoms", [])) or "None")
                c3, c4 = st.columns(2)
                c3.metric("⚖️ Dosages", ", ".join(entities.get("Dosage", [])) or "None")
                c4.metric("⏱️ Frequencies", ", ".join(entities.get("Frequency", [])) or "None")
        else:
            st.info("Provide text or an image on the left to begin.")

elif menu == "2. Disease Prediction":
    st.title("🩺 2. AI Disease Prediction")
    st.markdown("Predict potential diseases based on symptoms.")
    
    st.info("You can type symptoms below. Extracted symptoms from the prescription are pre-loaded.")
    default_symps = ", ".join(get_ner_list("Symptoms"))
    
    symptoms_input = st.text_input("Enter symptoms (comma-separated):", value=default_symps)
    
    if st.button("Predict Disease", type="primary"):
        symptom_list = [s.strip() for s in symptoms_input.split(",") if s.strip()]
        if not symptom_list:
            st.warning("Please enter at least one symptom.")
        else:
            with st.spinner("Analyzing symptoms..."):
                try:
                    res = api_post_predict(symptom_list)
                    preds = res.get("predictions", [])
                    st.session_state.shared_data['prediction_results'] = preds
                    
                    if preds:
                        st.subheader("Top Predictions")
                        cols = st.columns(len(preds))
                        for idx, p in enumerate(preds):
                            with cols[idx]:
                                with st.container(border=True):
                                    st.markdown(f"### {p['disease'].title().replace('_', ' ')}")
                                    st.metric("Probability", p['probability'])
                                    st.caption(f"Confidence: {p['confidence']}")
                    else:
                        st.warning("No strong predictions found for these symptoms.")
                except Exception as e:
                    st.error(f"Prediction Error: {e}")

elif menu == "3. Drug Interactions":
    st.title("⚡ 3. Drug Interaction Check")
    st.markdown("Use Google Gemini AI to analyze interactions between multiple medications.")
    
    meds = get_ner_list("Medication")
    med_input = st.text_area("Medications to check (comma-separated):", value=", ".join(meds))
    
    if st.button("Check Interactions", type="primary"):
        med_list = [m.strip() for m in med_input.split(",") if m.strip()]
        if len(med_list) < 2:
            st.warning("Please enter at least 2 medications to check interactions.")
        else:
            with st.spinner("AI is analyzing drug interactions..."):
                try:
                    res = api_post_interactions(med_list)
                    st.session_state.shared_data['interaction_results'] = res
                    with st.container(border=True):
                        st.markdown(res)
                except Exception as e:
                    st.error(f"Interaction Error: {e}")

elif menu == "4. Verification & Dosage":
    st.title("✅ 4. Drug Safety & Dosage Guidelines")
    st.markdown(f"**Patient Context:** Age: {patient_age_yrs} yrs ({patient_age_months} months) | Weight: {patient_weight_kg} kg")
    
    tab1, tab2 = st.tabs(["Safety Verification", "Dosage Guidelines"])
    
    with tab1:
        st.subheader("Verify Prescription Safety")
        col1, col2, col3 = st.columns(3)
        with col1: v_med = st.text_input("Medication", value=get_ner_first("Medication"), key="v1")
        with col2: v_symp = st.text_input("Symptom", value=get_ner_first("Symptoms"), key="v2")
        with col3: 
            v_dose_str = st.text_input("Prescribed Dose (e.g., '500 mg')", value=get_ner_first("Dosage"), key="v3")
            
        if st.button("Run Verification", type="primary"):
            if not (v_med and v_symp and v_dose_str):
                st.warning("Fill all fields.")
            else:
                try:
                    # Extract raw number from dosage string
                    match = re.search(r'(\d+\.?\d*)', v_dose_str)
                    if not match: raise ValueError("No number found in dosage.")
                    given_mg = float(match.group(1))
                    dose_mg_kg = given_mg / patient_weight_kg
                    
                    with st.spinner("Cross-referencing datasets..."):
                        report = api_get_verify(v_symp, v_med, patient_age_months, dose_mg_kg)
                        st.session_state.shared_data['verify_results'] = report
                        
                        st.markdown(f"**Calculated Dose:** `{dose_mg_kg:.2f} mg/kg`")
                        r_col1, r_col2, r_col3 = st.columns(3)
                        r_col1.metric("Symptom Check", "✅ Pass" if "Pass" in report.get("symptom_check","") else "⚠️ Warn/Fail", help=report.get("symptom_check"))
                        r_col2.metric("Age Check", "✅ Pass" if "Pass" in report.get("age_check","") else "⚠️ Warn/Fail", help=report.get("age_check"))
                        r_col3.metric("Dosage Check", "✅ Pass" if "Pass" in report.get("dosage_check","") else "⚠️ Warn/Fail", help=report.get("dosage_check"))
                        
                        if report.get("notes"):
                            st.info("**Notes:**\n" + "\n".join([f"- {n}" for n in report.get("notes")]))
                except Exception as e:
                    st.error(f"Error checking verification: {e}")
                    
    with tab2:
        st.subheader("Lookup Standard Dosage")
        d_med = st.text_input("Medication Name", value=get_ner_first("Medication"), key="d1")
        if st.button("Fetch Guidelines"):
            with st.spinner("Fetching..."):
                try:
                    res = api_get_dosage(d_med, patient_age_months)
                    st.session_state.shared_data['dosage_results'] = res
                    
                    with st.container(border=True):
                        st.markdown(f"### 💊 {res.get('drug_generic', d_med)}")
                        c1, c2 = st.columns(2)
                        c1.metric("Max Daily Dose", f"{res.get('max_daily_dose')} {res.get('max_daily_dose_units')}")
                        c2.metric("Dosing Interval", f"Every {res.get('dosing_interval_hours')} hours")
                        st.warning(f"**Safety Note:** {res.get('notes_key_safety', 'N/A')}")
                except Exception as e:
                    st.error(f"Error fetching dosage (check if medicine exists in dataset): {e}")

elif menu == "5. Cost & Alternatives":
    st.title("💸 5. Cost Savings & Home Remedies")
    
    a_med = st.text_input("Enter Medication Name to search for cheaper alternatives:", value=get_ner_first("Medication"))
    
    if st.button("Find Alternatives", type="primary"):
        with st.spinner("Searching database..."):
            try:
                res = api_get_alternatives(a_med)
                if not res:
                    st.warning("No alternatives found in the database for this medicine.")
                else:
                    st.session_state.shared_data['alt_results'] = res
                    base_price = res.get('price_in_inr', 0)
                    
                    st.markdown(f"### {a_med.title()} (Base Price: ₹{base_price})")
                    st.caption(res.get('description', ''))
                    
                    col_alt, col_rem = st.columns(2)
                    with col_alt:
                        st.subheader("💊 Generic Alternatives")
                        for alt in res.get('alternatives', []):
                            with st.expander(f"**{alt['name']}** - ₹{alt['price_in_inr']}"):
                                st.metric("Savings", f"{alt['savings_percentage']}%")
                    
                    with col_rem:
                        st.subheader("🌿 Home Remedies")
                        for cond, rem in res.get('home_remedies_for_common_uses', {}).items():
                            st.markdown(f"- **{cond}**: {rem}")
                            
                    st.info(f"**Note:** {res.get('notes', '')}")
            except Exception as e:
                st.error(f"API Error: {e}")

elif menu == "6. AI Final Summary":
    st.title("🤖 6. AI Patient Summary")
    st.markdown("Generates a comprehensive summary using all data processed in the previous steps.")
    
    st.write("Data ready for synthesis:")
    flags = {
        "NER Data": bool(st.session_state.shared_data['ner_results']),
        "Verification Data": bool(st.session_state.shared_data['verify_results']),
        "Interactions": bool(st.session_state.shared_data['interaction_results']),
        "Alternatives": bool(st.session_state.shared_data['alt_results'])
    }
    
    cols = st.columns(4)
    for i, (k, v) in enumerate(flags.items()):
        cols[i].metric(k, "Ready" if v else "Empty")
        
    if st.button("Generate Final Report", type="primary", use_container_width=True):
        outputs_to_send = []
        for k, v in st.session_state.shared_data.items():
            if v and k != "extracted_text": # Send all JSON/structured data
                outputs_to_send.append({k: v})
                
        if not outputs_to_send:
            st.error("No data available to summarize. Please run the other steps first.")
        else:
            with st.spinner("Gemini AI is crafting the summary..."):
                try:
                    summary = api_post_summary(outputs_to_send)
                    with st.container(border=True):
                        st.markdown(summary)
                except Exception as e:
                    st.error(f"Summarizer Error: {e}")
