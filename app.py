# app.py

import streamlit as st
from transformers import pipeline
# Import your feature modules that contain ONLY pure Python logic
from features import ocr, ner

# --- App UI Configuration ---
st.set_page_config(layout="wide", page_title="Medical Prescription Analyzer")
st.title("⚕️ Medical Prescription Analyzer")
st.markdown("A tool to automatically extract structured data from medical prescriptions.")

# --- Caching and Resource Loading (Handled ONLY by the App) ---
@st.cache_resource
def load_ner_model():
    """Loads the Hugging Face NER model and caches it using Streamlit."""
    model = pipeline("ner", model="d4data/biomedical-ner-all", aggregation_strategy="simple")
    return model

@st.cache_resource
def load_gcp_vision_client():
    """Loads the Google Cloud Vision client and caches it using Streamlit."""
    try:
        # st.secrets reads from your .streamlit/secrets.toml file
        return ocr.get_gcp_vision_client(st.secrets["gcp_service_account"])
    except Exception as e:
        # This will now display a more prominent error if secrets are wrong
        st.error(f"Could not load Google Cloud Vision client. Please check your secrets.toml file. Error: {e}")
        return None

# --- Load Models and Clients into memory ---
with st.sidebar:
    st.header("System Status")
    ner_pipeline = load_ner_model()
    vision_client = load_gcp_vision_client() # Load the client

    if ner_pipeline:
        st.success("NER Model loaded.")
    else:
        st.error("NER Model failed to load.")

    if vision_client:
        st.success("GCP Vision Client loaded.")
    else:
        st.error("GCP Vision Client failed to load. Check secrets.")


# --- Main Application Logic ---
# Add a safety check. If the vision client failed to load, stop the app.
if not vision_client:
    st.warning("OCR functionality is disabled because the Google Cloud Vision Client could not be initialized. Please check your credentials in the `.streamlit/secrets.toml` file.")
    st.stop() # This is the key command to prevent the crash.

text_to_process = ""
input_source = None

st.header("1. Provide Prescription")
tab1, tab2, tab3 = st.tabs(["📁 Upload Image", "📸 Take Photo", "✍️ Type Text"])

with tab1:
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        input_source = "image"
        text_to_process = ocr.extract_text_from_bytes(vision_client, uploaded_file.getvalue())

with tab2:
    camera_photo = st.camera_input("Take a photo", label_visibility="collapsed")
    if camera_photo:
        input_source = "camera"
        text_to_process = ocr.extract_text_from_bytes(vision_client, camera_photo.getvalue())

with tab3:
    manual_text = st.text_area("Or, paste the prescription text here:", height=200, key="manual_text_input",
                               placeholder="e.g., Take Paracetamol 500mg twice a day for fever.")
    if manual_text:
        text_to_process = manual_text
        input_source = "text"

# --- Analysis and Display Section ---
if text_to_process:
    st.divider()
    st.header("2. Analysis Results")

    if input_source in ["image", "camera"]:
         with st.expander("Show Raw Text Extracted from Image (OCR)"):
             st.text(text_to_process)
    
    with st.spinner("Analyzing text for medical entities..."):
        extracted_data = ner.extract_medical_entities(text_to_process, ner_pipeline)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Formatted View")
            for key, value in extracted_data.items():
                st.markdown(f"**{key.capitalize()}:**")
                if value:
                    for item in value:
                        st.markdown(f"- `{item}`")
                else:
                    st.markdown("  - *N/A*")
        with col2:
            st.subheader("JSON View")
            st.json(extracted_data)
else:
    st.info("Please provide a prescription by uploading an image, taking a photo, or typing text.")