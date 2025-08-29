# app.py

import streamlit as st
from transformers import pipeline
import requests
import re
from features import ocr, ner
from backend.data_processors import prescription

# --- API Configuration ---
API_BASE_URL = "http://127.0.0.1:8000" # IMPORTANT: Update with your friend's FastAPI URL

# --- App UI Configuration ---
st.set_page_config(layout="wide", page_title="Medify - Medical Prescription Analyzer")
st.title("⚕️ Medify: Prescription Analysis & Verification")
st.markdown("An intelligent tool to extract, analyze, and verify medical prescriptions.")

# --- Caching and Resource Loading ---
@st.cache_resource
def load_ner_model():
    """Loads the Hugging Face NER model and caches it."""
    model = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")
    return model

@st.cache_resource
def load_gcp_vision_client():
    """Loads the Google Cloud Vision client and caches it."""
    try:
        return ocr.get_gcp_vision_client(st.secrets["gcp_service_account"])
    except Exception as e:
        st.error(f"Could not load Google Cloud Vision client. Check secrets.toml. Error: {e}")
        return None

# --- Load Models and Clients into memory ---
with st.sidebar:
    st.header("System Status")
    ner_pipeline = load_ner_model()
    vision_client = load_gcp_vision_client()
    if ner_pipeline and vision_client:
        st.success("Services Ready!")
    else:
        st.error("A service failed to load.")

# --- Patient Profile Input in Sidebar ---
st.sidebar.divider()
st.sidebar.header("Patient Profile")
patient_age_years = st.sidebar.number_input("Patient Age (for Verification)", min_value=0, max_value=120, value=5, step=1)
patient_age_months = patient_age_years * 12

# --- Main Application Logic ---
st.header("1. Provide Prescription")
col1, col2 = st.columns([0.6, 0.4]) # Create two columns for input and NER results

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

# --- NER Analysis and Display ---
with col2:
    st.subheader("Extracted Information (NER)")
    if text_to_process:
        with st.spinner("Extracting entities..."):
            ner_data = ner.extract_medical_entities(text_to_process, ner_pipeline)

            # Display formatted view directly as requested
            for key, value in ner_data.items():
                st.markdown(f"**{key.capitalize()}:**")
                if value:
                    st.markdown(f"> `{' | '.join(value)}`")
                else:
                    st.markdown("> *N/A*")
    else:
        st.info("Results of the automated extraction will appear here once you provide an input.")

# --- Independent Verification Module ---
st.divider()
st.header("2. Verify Prescription Details")
st.markdown("Use the automatically extracted data or enter your own to verify against the backend service.")

# Pre-fill with NER data, but allow user edits
med_to_verify = ner_data.get("Medication")[0] if 'ner_data' in locals() and ner_data.get("Medication") else ""
symptom_to_verify = ner_data.get("Symptoms")[0] if 'ner_data' in locals() and ner_data.get("Symptoms") else ""
dosage_str_to_verify = ner_data.get("Dosage")[0] if 'ner_data' in locals() and ner_data.get("Dosage") else ""

verify_col1, verify_col2, verify_col3, verify_col4 = st.columns(4)
with verify_col1:
    med_input = st.text_input("Medication to Verify", value=med_to_verify)
with verify_col2:
    symptom_input = st.text_input("Symptom", value=symptom_to_verify)
with verify_col3:
    dosage_input = st.text_input("Dosage", value=dosage_str_to_verify, help="e.g., '500mg' or '10ml'")
with verify_col4:
    # This makes the mg/kg calculation transparent
    assumed_weight = st.number_input("Assumed Weight (kg) for Calc", min_value=1.0, value=20.0, step=0.5)

if st.button("Run Verification", type="primary", use_container_width=True):
    if not all([med_input, symptom_input, dosage_input]):
        st.error("Please fill in the Medication, Symptom, and Dosage fields to run verification.")
    else:
        with st.spinner(f"Verifying '{med_input.capitalize()}'..."):
            try:
                given_mg = float(re.search(r'(\d+\.?\d*)', dosage_input).group(1))
                given_dosage_mg_per_kg = given_mg / assumed_weight

                # Construct the API call
                endpoint = f"{API_BASE_URL}/drug_info/verify"
                params = {
                    "symptom": symptom_input,
                    "medicine_name": med_input,
                    "age_in_months": patient_age_months,
                    "given_dosage_mg_per_kg": given_dosage_mg_per_kg
                }
                
                response = requests.get(endpoint, params=params)
                response.raise_for_status()
                verification_result = response.json()

                # --- NEW: Enhanced UI for Verification Results ---
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

                st.info(f"**Notes from Verification Service:**\n- {' | '.join(verification_result.get('notes', []))}")
                st.caption(f"**Disclaimer:** {verification_result.get('disclaimer', '')}")


            except requests.exceptions.RequestException as e:
                st.error(f"**API Connection Error:** Could not connect to the verification service. Please ensure the backend is running. Details: {e}")
            except (AttributeError, ValueError):
                 st.error(f"**Input Error:** Could not parse a valid number from the dosage string: '{dosage_input}'. Please enter a value like '500mg'.")