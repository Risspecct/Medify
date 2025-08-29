# app.py

import streamlit as st
from transformers import pipeline
import requests
import re
import os
from features import ocr, ner, alternative
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- API Configuration ---
API_BASE_URL = os.getenv("FAST_API_URL")  # IMPORTANT: Update with your friend's deployed FastAPI URL

# --- App UI Configuration ---
st.set_page_config(layout="wide", page_title="Medify - Medical Prescription Analyzer")
st.title("⚕️ Medify: Prescription Analysis & Verification")
st.markdown("An intelligent tool to extract, analyze, and verify medical prescriptions.")


# --- Caching and Resource Loading ---
@st.cache_resource
def load_ner_model():
    model = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")
    return model


@st.cache_resource
def load_gcp_vision_client():
    try:
        return ocr.get_gcp_vision_client(st.secrets["gcp_service_account"])
    except Exception as e:
        st.error(f"Could not load Google Cloud Vision client. Check secrets.toml. Error: {e}")
        return None


# --- Initialize Session State ---
if 'dosage_result' not in st.session_state:
    st.session_state.dosage_result = None
if 'last_med_checked' not in st.session_state:
    st.session_state.last_med_checked = ""
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'last_alt_med_checked' not in st.session_state:
    st.session_state.last_alt_med_checked = ""


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
col1, col2 = st.columns([0.6, 0.4])
# ... (Input and NER sections are unchanged) ...
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
    st.subheader("Extracted Information (NER)")
    if text_to_process:
        with st.spinner("Extracting entities..."):
            ner_data = ner.extract_medical_entities(text_to_process, ner_pipeline)
            for key, value in ner_data.items():
                st.markdown(f"**{key.capitalize()}:**")
                if value:
                    st.markdown(f"> `{' | '.join(value)}`")
                else:
                    st.markdown("> *N/A*")
    else:
        st.info("Results of automated extraction will appear here.")
med_input_default = ner_data.get("Medication")[0] if 'ner_data' in locals() and ner_data.get("Medication") else ""
symptom_input_default = ner_data.get("Symptoms")[0] if 'ner_data' in locals() and ner_data.get("Symptoms") else ""
dosage_input_default = ner_data.get("Dosage")[0] if 'ner_data' in locals() and ner_data.get("Dosage") else ""

# --- Independent Verification Module ---
st.divider()
st.header("2. Verify Prescription Details")
# ... (Verification module is unchanged) ...
st.markdown("Use the automatically extracted data or enter your own to verify against the backend service.")
verify_col1, verify_col2, verify_col3, verify_col4 = st.columns(4)
with verify_col1:
    med_input = st.text_input("Medication to Verify", value=med_input_default)
with verify_col2:
    symptom_input = st.text_input("Symptom", value=symptom_input_default)
with verify_col3:
    dosage_input = st.text_input("Dosage", value=dosage_input_default, help="e.g., '500mg' or '10ml'")
with verify_col4:
    assumed_weight = st.number_input("Assumed Weight (kg) for Calc", min_value=1.0, value=20.0, step=0.5)
if st.button("Run Verification", type="primary", use_container_width=True):
    if not all([med_input, symptom_input, dosage_input]):
        st.error("Please fill in the Medication, Symptom, and Dosage fields to run verification.")
    else:
        with st.spinner(f"Verifying '{med_input.capitalize()}'..."):
            try:
                given_mg = float(re.search(r'(\d+\.?\d*)', dosage_input).group(1))
                given_dosage_mg_per_kg = given_mg / assumed_weight
                endpoint = f"{API_BASE_URL}/drug_info/verify"
                params = {"symptom": symptom_input, "medicine_name": med_input, "age_in_months": patient_age_months, "given_dosage_mg_per_kg": given_dosage_mg_per_kg}
                response = requests.get(endpoint, params=params)
                response.raise_for_status()
                verification_result = response.json()
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
                st.error(f"**API Connection Error:** Could not connect to the verification service. Details: {e}")
            except (AttributeError, ValueError):
                st.error(f"**Input Error:** Could not parse a valid number from the dosage string: '{dosage_input}'.")

# --- Independent Dosage Recommendation Module ---
st.divider()
st.header("3. Fetch Dosage Guidelines")
# ... (Dosage recommendation module is unchanged) ...
st.markdown("Get standard dosage information for a specific medication and age from the backend service.")
rec_col1, rec_col2 = st.columns([0.8, 0.2])
with rec_col1:
    dosage_med_input = st.text_input("Medication Name", value=med_input, key="dosage_med_input", help="Enter a medication name to get its standard dosage guidelines.")
if dosage_med_input != st.session_state.last_med_checked:
    st.session_state.dosage_result = None
    st.session_state.last_med_checked = dosage_med_input
with rec_col2:
    st.write("")
    disable_fetch_button = (st.session_state.dosage_result is not None)
    if st.button("Fetch Dosage Info", use_container_width=True, disabled=disable_fetch_button):
        if not dosage_med_input:
            st.error("Please enter a medication name.")
        else:
            with st.spinner(f"Fetching guidelines for '{dosage_med_input.capitalize()}'..."):
                try:
                    endpoint = f"{API_BASE_URL}/drug_info/dosage/{dosage_med_input}/{patient_age_months}"
                    response = requests.get(endpoint)
                    response.raise_for_status()
                    st.session_state.dosage_result = response.json()
                except requests.exceptions.RequestException as e:
                    st.error(f"API Connection Error: {e}")
                    st.session_state.dosage_result = None
if st.session_state.dosage_result:
    result = st.session_state.dosage_result
    if result and result.get("drug_generic"):
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
        st.warning(f"Could not find dosage information for **'{dosage_med_input}'** in the database.")

# --- NEW: Independent Alternative Recommendations Module with Corrected UI Layout ---
st.divider()
st.header("4. Find Alternative Medications & Remedies")
st.markdown("Get suggestions for alternative medications and home remedies for a given drug.")

# --- THIS IS THE CORRECTED LAYOUT ---
# The input field and button are now in the main container, not columns.
alt_med_input = st.text_input("Medication Name", value=med_input, key="alt_med_input",
                              help="Enter a medication to find potential alternatives.")

if st.button("Find Alternatives", use_container_width=True):
    # Clear previous results when a new search is made
    st.session_state.recommendations = None
    if not alt_med_input:
        st.error("Please enter a medication name to get recommendations.")
    else:
        # We store the result in session state to persist it across reruns
        st.session_state.recommendations = alternative.find_alternatives(alt_med_input)
        st.session_state.last_alt_med_checked = alt_med_input

# Display the results card ONLY if there are recommendations to show
if st.session_state.recommendations:
    recommendations = st.session_state.recommendations

    # Check if the result is for the currently displayed medication name
    if st.session_state.last_alt_med_checked == alt_med_input:
        with st.container(border=True):
            st.markdown(f"#### 💡 Alternatives & Remedies for **{alt_med_input.capitalize()}**")
            st.markdown(f"*{recommendations.get('description', '')}*")
            st.divider()

            # These columns are now inside the main container and will have enough space
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
    else:
        # This handles the case where the user types a new med name but hasn't clicked the button yet
        st.session_state.recommendations = None

elif 'recommendations' in st.session_state and st.session_state.recommendations is None and st.session_state.last_alt_med_checked:
    # This displays the "not found" message after a search
    if st.session_state.last_alt_med_checked == alt_med_input:
        st.info(f"No specific alternatives found for '{alt_med_input}' in our knowledge base.")
