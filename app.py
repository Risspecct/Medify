# app.py

import streamlit as st
from transformers import pipeline
import requests
import json
import re
import os
# Import all your feature modules
from features import ocr, ner, alternative, ai_services, verification_client
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# --- API Configuration ---
API_BASE_URL = os.getenv("FAST_API_URL", "http://127.0.0.1:8000")
# Set the base URL for all client modules
ai_services.API_BASE_URL = API_BASE_URL
verification_client.API_BASE_URL = API_BASE_URL

# --- App UI Configuration ---
st.set_page_config(layout="wide", page_title="Medify - AI Prescription Analyzer")
st.title("⚕️ Medify: AI-Powered Prescription Analysis")
st.markdown("An intelligent tool to extract, analyze, verify, and summarize medical prescriptions.")

# --- Initialize Session State ---
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = {}
if 'dosage_result' not in st.session_state:
    st.session_state.dosage_result = None
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

# --- Caching and Resource Loading ---
@st.cache_resource
def load_ner_model():
    return pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")

@st.cache_resource
def load_gcp_vision_client():
    try:
        # Check for Render environment variable first
        gcp_json_str = os.getenv("GCP_SERVICE_ACCOUNT_JSON")
        if gcp_json_str:
            credentials_info = json.loads(gcp_json_str)
        # Fallback to local secrets.toml for local development
        else:
            credentials_info = st.secrets["gcp_service_account"]
        return ocr.get_gcp_vision_client(credentials_info)
    except Exception as e:
        st.error(f"Could not load Google Cloud Vision client. Check secrets/environment variables. Error: {e}")
        return None

# --- Load Models and Clients into memory ---
with st.sidebar:
    st.header("System Status")
    ner_pipeline = load_ner_model()
    vision_client = load_gcp_vision_client()
    if ner_pipeline and vision_client: st.success("Services Ready!")
    else: st.error("A service failed to load.")

# --- Patient Profile Input in Sidebar ---
st.sidebar.divider()
st.sidebar.header("Patient Profile")
patient_age_years = st.sidebar.number_input("Patient Age (Years)", min_value=0, max_value=120, value=5, step=1)
st.session_state.analysis_results['patient_profile'] = {'age_years': patient_age_years}

# --- Main Application Logic ---
# 1. OCR AND NER
st.header("1. Extract Information from Prescription")
col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.subheader("Input")
    text_to_process = ""
    tab1, tab2, tab3 = st.tabs(["📁 Upload Image", "📸 Take Photo", "✍️ Type Text"])
    with tab1:
        uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
        if uploaded_file:
            text_to_process = ocr.extract_text_from_bytes(vision_client, uploaded_file.getvalue())
    with tab2:
        camera_photo = st.camera_input("Take a photo", label_visibility="collapsed")
        if camera_photo:
            text_to_process = ocr.extract_text_from_bytes(vision_client, camera_photo.getvalue())
    with tab3:
        manual_text = st.text_area("Or, paste the prescription text here:", height=200, key="manual_text_input")
        if manual_text:
            text_to_process = manual_text
with col2:
    st.subheader("Extracted Entities (NER)")
    if text_to_process:
        with st.spinner("Extracting entities..."):
            ner_data = ner.extract_medical_entities(text_to_process, ner_pipeline)
            st.session_state.analysis_results['ner_results'] = ner_data
            for key, value in ner_data.items():
                st.markdown(f"**{key.capitalize()}:**")
                if value: st.markdown(f"> `{' | '.join(value)}`")
                else: st.markdown("> *N/A*")
    else:
        st.info("Results of automated extraction will appear here.")

med_input_default = st.session_state.analysis_results.get('ner_results', {}).get("Medication", [""])[0]
symptom_input_default = st.session_state.analysis_results.get('ner_results', {}).get("Symptoms", [""])[0]
dosage_input_default = st.session_state.analysis_results.get('ner_results', {}).get("Dosage", [""])[0]

# 2. AI DRUG INTERACTIONS
st.divider()
st.header("2. AI Drug Interaction Analysis")
st.markdown("Check for potential interactions between the extracted medications using the AI backend.")
if st.button("Check Interactions", use_container_width=True, key="interaction_button"):
    meds = st.session_state.analysis_results.get('ner_results', {}).get("Medication", [])
    if len(meds) < 2:
        st.info("At least two medications must be extracted to check for interactions.")
    else:
        with st.spinner(f"Contacting AI to check interactions for {', '.join(meds)}..."):
            interaction_data = ai_services.call_interaction_api(meds)
            st.session_state.analysis_results['interaction_report'] = interaction_data
            with st.container(border=True):
                st.markdown(interaction_data, unsafe_allow_html=True)

# 3. VERIFICATION
st.divider()
st.header("3. Manual Verification")
st.markdown("Manually verify a specific drug against the backend dataset for symptom, age, and dosage.")
verify_col1, verify_col2, verify_col3, verify_col4 = st.columns(4)
with verify_col1:
    med_input = st.text_input("Medication", value=med_input_default, key="verify_med")
with verify_col2:
    symptom_input = st.text_input("Symptom", value=symptom_input_default, key="verify_symptom")
with verify_col3:
    dosage_input = st.text_input("Dosage", value=dosage_input_default, key="verify_dosage")
with verify_col4:
    weight_input = st.number_input("Patient Weight (kg)", min_value=1.0, value=30.0, step=0.5, key="verify_weight")
if st.button("Run Verification", use_container_width=True, key="verify_button"):
    if not all([med_input, symptom_input, dosage_input]):
        st.error("Please fill in all fields to run verification.")
    else:
        with st.spinner("Verifying..."):
            try:
                given_mg = float(re.search(r'(\d+\.?\d*)', dosage_input).group(1))
                params = {"symptom": symptom_input, "medicine_name": med_input, "age_in_months": patient_age_years * 12, "given_dosage_mg_per_kg": given_mg / weight_input}
                verification_result = verification_client.call_verify_api(params)
                if verification_result and isinstance(verification_result, dict):
                    st.session_state.analysis_results['verification_report'] = verification_result
                    st.subheader("Verification Report")
                    res_col1, res_col2, res_col3 = st.columns(3)
                    with res_col1:
                        symptom_res = verification_result.get("symptom_check", "Error")
                        symptom_status = "✅ Pass" if "pass" in symptom_res.lower() else "⚠️ Warn"
                        st.metric(label="Symptom Match", value=symptom_status, help=symptom_res)
                    with res_col2:
                        age_res = verification_result.get("age_check", "Error")
                        age_status = "✅ Pass" if "pass" in age_res.lower() else ("⚠️ Warn" if "not applicable" in age_res.lower() else "❌ Fail")
                        st.metric(label="Age Appropriateness", value=age_status, help=age_res)
                    with res_col3:
                        dosage_res = verification_result.get("dosage_check", "Error")
                        dosage_status = "✅ Pass" if "pass" in dosage_res.lower() else ("⚠️ Warn" if "not applicable" in dosage_res.lower() else "❌ Fail")
                        st.metric(label="Dosage Safety", value=dosage_status, help=dosage_res)
                else:
                    st.error("Verification failed. The backend did not return a valid result.")
            except (AttributeError, ValueError):
                st.error(f"Input Error: Could not parse a valid number from the dosage string: '{dosage_input}'.")

# 4. DOSAGE GUIDELINES
st.divider()
st.header("4. Fetch Dosage Guidelines")
st.markdown("Get standard dosage information for a specific medication and age.")
dose_col1, dose_col2 = st.columns([0.8, 0.2])
with dose_col1:
    dosage_med_input = st.text_input("Medication Name", value=med_input_default, key="dosage_med_input")
with dose_col2:
    st.write("")
    if st.button("Fetch Dosage Info", use_container_width=True, key="dosage_button"):
        if dosage_med_input:
            with st.spinner("Fetching guidelines..."):
                dosage_result = verification_client.call_dosage_api(dosage_med_input, patient_age_years * 12)
                st.session_state.dosage_result = dosage_result
if st.session_state.dosage_result:
    result = st.session_state.dosage_result
    if isinstance(result, dict) and result.get("drug_generic"):
        st.session_state.analysis_results['dosage_guidelines'] = result
        with st.container(border=True):
            drug_name = result.get('drug_generic', 'N/A')
            st.markdown(f"#### 💊 Dosage Guidelines for **{drug_name}**")
            st.divider()
            d_col1, d_col2 = st.columns(2)
            with d_col1:
                max_dose = result.get('max_daily_dose', 'N/A')
                units = result.get('max_daily_dose_units', '')
                st.metric(label="⚖️ Max Daily Dose", value=f"{max_dose} {units}")
            with d_col2:
                interval = result.get('dosing_interval_hours', 'N/A')
                st.metric(label="⏰ Dosing Interval", value=f"Every {interval} hours")
            st.warning(f"**⚠️ Key Safety Notes:** {result.get('notes_key_safety', 'No specific safety notes found.')}")
    else:
        st.warning(f"Could not find valid dosage information for **'{st.session_state.get('dosage_med_input', '')}'**.")

# 5. ALTERNATIVE REMEDIES
st.divider()
st.header("5. Find Alternative Remedies & OTC Options")
st.markdown("Get suggestions for alternative medications and home remedies for a given drug.")
alt_med_input = st.text_input("Medication Name", value=med_input_default, key="alt_med_input")
if st.button("Find Alternatives", use_container_width=True, key="alt_button"):
    if alt_med_input:
        recommendations = alternative.find_alternatives(alt_med_input)
        st.session_state.recommendations = recommendations
        st.session_state.analysis_results['alternatives_report'] = recommendations

# --- THIS IS THE CORRECTED AND FINAL UI LOGIC FOR ALTERNATIVES ---
if st.session_state.get('recommendations'):
    recommendations = st.session_state.recommendations
    with st.container(border=True):
        st.markdown(f"#### 💡 Alternatives & Remedies for **{alt_med_input.capitalize()}**")
        st.markdown(f"*{recommendations.get('description', '')}*")
        st.divider()

        alt_rec_col1, alt_rec_col2 = st.columns(2)
        with alt_rec_col1:
            st.subheader("💊 Medication Alternatives")
            alts = recommendations.get('alternatives', [])
            if alts:
                for alt in alts:
                    if '(' in alt:
                        name, desc = alt.split('(', 1)
                        st.markdown(f"**{name.strip()}**")
                        st.caption(f"({desc.strip()}")
                    else:
                        st.markdown(f"**{alt.strip()}**")
            else:
                st.markdown("No specific medication alternatives listed.")
        with alt_rec_col2:
            st.subheader("🌿 Home Remedies")
            remedies = recommendations.get('home_remedies_for_common_uses', {})
            if remedies:
                for use, remedy in remedies.items():
                    st.markdown(f"**{use}:** {remedy}")
            else:
                st.markdown("No specific home remedies listed.")
        st.divider()
        st.warning(f"**⚠️ Important Notes:** {recommendations.get('notes', '')}")
elif st.session_state.get('recommendations') is False:
    st.info(f"No specific alternatives found for '{alt_med_input}' in our knowledge base.")

# 6. AI-POWERED SUMMARY
st.divider()
st.header("6. Generate Final AI-Powered Summary")
st.markdown("This will synthesize all the analysis performed above into a single, cohesive patient summary.")
if st.button("Generate AI Summary", type="primary", use_container_width=True, key="summary_button"):
    if not st.session_state.analysis_results.get('ner_results'):
        st.error("Cannot generate a summary. Please provide a prescription to extract entities first.")
    else:
        with st.spinner("Synthesizing data with the AI backend..."):
            summary_text = ai_services.call_summary_api(st.session_state.analysis_results)
            st.session_state.analysis_results['final_summary'] = summary_text
            with st.container(border=True):
                st.subheader("🤖 Your AI-Generated Patient Summary")
                st.markdown(summary_text)