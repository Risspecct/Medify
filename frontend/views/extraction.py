import streamlit as st
from api import ocr_extract, ner_parse
from ui_core import render_pill

def render():
    st.title("📄 Step 1: Digitization & Extraction")
    st.markdown("Upload a prescription image. Medify will read the text and extract key medical entities automatically.")
    
    col_input, col_output = st.columns([1, 1.2], gap="large")
    
    with col_input:
        st.markdown("#### 📥 Input Source")
        
        tab1, tab2, tab3 = st.tabs(["Upload Image", "Camera", "Manual Text"])
        extracted_text = ""
        
        with tab1:
            img_file = st.file_uploader("Upload Prescription", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
            if img_file and st.button("Extract Text", use_container_width=True):
                with st.spinner("Processing image via GCP Vision..."):
                    try:
                        res = ocr_extract(img_file)
                        extracted_text = res.get("extracted_text", "")
                        st.session_state.app_data['extracted_text'] = extracted_text
                        st.success("Image text extracted!")
                    except Exception as e:
                        st.error(f"OCR Error: {e}")
                        
        with tab2:
            cam_file = st.camera_input("Take a photo", label_visibility="collapsed")
            if cam_file and st.button("Extract from Camera", use_container_width=True):
                with st.spinner("Processing image..."):
                    try:
                        res = ocr_extract(cam_file)
                        extracted_text = res.get("extracted_text", "")
                        st.session_state.app_data['extracted_text'] = extracted_text
                        st.success("Image text extracted!")
                    except Exception as e:
                        st.error(f"OCR Error: {e}")
                        
        with tab3:
            manual_text = st.text_area("Paste text manually:", value=st.session_state.app_data.get('extracted_text', ''), height=200)
            if st.button("Use Entered Text", use_container_width=True):
                extracted_text = manual_text
                st.session_state.app_data['extracted_text'] = extracted_text
                
        if st.session_state.app_data.get('extracted_text'):
            with st.expander("View Raw Extracted Text"):
                st.text(st.session_state.app_data['extracted_text'])

    with col_output:
        st.markdown("#### 🧠 Extracted Entities")
        
        if st.session_state.app_data.get('extracted_text'):
            if st.button("Run AI Extraction (NER)", type="primary", use_container_width=True):
                with st.spinner("Parsing medical entities..."):
                    try:
                        ner_res = ner_parse(st.session_state.app_data['extracted_text'])
                        st.session_state.app_data['ner_results'] = ner_res.get("entities", {})
                    except Exception as e:
                        st.error(f"NER Error: {e}")
            
            entities = st.session_state.app_data.get('ner_results', {})
            if entities:
                with st.container(border=True):
                    st.markdown("**💊 Medications**")
                    meds = entities.get("Medication", [])
                    st.markdown(" ".join([render_pill(m) for m in meds]) if meds else "*None found*", unsafe_allow_html=True)
                    
                    st.markdown("<br>**🤒 Symptoms**", unsafe_allow_html=True)
                    symps = entities.get("Symptoms", [])
                    st.markdown(" ".join([render_pill(s) for s in symps]) if symps else "*None found*", unsafe_allow_html=True)
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("**⚖️ Dosages**")
                        for d in entities.get("Dosage", []): st.markdown(f"- {d}")
                    with c2:
                        st.markdown("**⏱️ Frequencies**")
                        for f in entities.get("Frequency", []): st.markdown(f"- {f}")
        else:
            st.info("👈 Upload an image or enter text to begin extraction.")