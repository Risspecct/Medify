import streamlit as st

def render():
    st.title("⚕️ Medify Overview")
    st.markdown("Welcome to your intelligent medical assistant. Use the sidebar to navigate through the analysis pipeline.")
    
    st.write("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📄 Digitization")
        st.write("Convert physical prescriptions into structured digital data using Google Vision OCR and advanced NLP/NER models.")
        
    with col2:
        st.markdown("### 🛡️ Safety Engine")
        st.write("Cross-reference prescribed dosages against pediatric & adult guidelines to flag overdoses, underdoses, or age mismatches.")
        
    with col3:
        st.markdown("### 🤖 AI Insights")
        st.write("Leverage Gemini AI to check complex drug interactions, summarize clinical data, and predict potential diseases.")

    st.write("---")
    st.subheader("Current Session Data")
    if st.session_state.app_data.get('ner_results'):
        st.success("Prescription data loaded and active. Ready for analysis.")
        st.json(st.session_state.app_data['ner_results'])
    else:
        st.info("No active prescription data. Head over to **1. Extraction** to upload a prescription.")
