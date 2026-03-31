import streamlit as st
import re
from api import verify_prescription, get_dosage

def render():
    st.title("✅ Step 4: Safety & Dosage Verification")
    
    # Display patient context clearly
    patient_age_yrs = st.session_state.patient_profile['age_years']
    patient_weight = st.session_state.patient_profile['weight_kg']
    patient_age_months = patient_age_yrs * 12
    
    st.info(f"👤 **Patient Profile:** {patient_age_yrs} Years Old | {patient_weight} kg")
    
    # Pre-fill from NER
    ner = st.session_state.app_data.get('ner_results', {})
    default_med = ner.get('Medication', [""])[0] if ner.get('Medication') else ""
    default_symp = ner.get('Symptoms', [""])[0] if ner.get('Symptoms') else ""
    default_dose = ner.get('Dosage', [""])[0] if ner.get('Dosage') else ""

    tab1, tab2 = st.tabs(["Safety Cross-Check", "View Guidelines"])
    
    with tab1:
        with st.container(border=True):
            st.markdown("#### Prescription Details")
            c1, c2, c3 = st.columns(3)
            with c1: v_med = st.text_input("Medication", value=default_med, key="v_med")
            with c2: v_symp = st.text_input("Symptom", value=default_symp, key="v_symp")
            with c3: v_dose = st.text_input("Given Dose (e.g., '500 mg')", value=default_dose, key="v_dose")
                
            if st.button("Run Safety Verification", type="primary"):
                if not (v_med and v_symp and v_dose):
                    st.warning("Please fill out all fields.")
                else:
                    try:
                        # Extract number safely
                        match = re.search(r'(\d+\.?\d*)', v_dose)
                        if not match: raise ValueError("Could not parse numeric value from dose.")
                        given_mg = float(match.group(1))
                        dose_mg_kg = given_mg / patient_weight
                        
                        with st.spinner("Validating against safety protocols..."):
                            report = verify_prescription(v_symp, v_med, patient_age_months, dose_mg_kg)
                            st.session_state.app_data['verify_results'] = report
                            
                            st.markdown("---")
                            st.markdown(f"**Administered Dose:** `{dose_mg_kg:.2f} mg/kg`")
                            
                            r1, r2, r3 = st.columns(3)
                            
                            # Helper to format cards
                            def format_status(text):
                                if "pass" in text.lower(): return "✅ Safe"
                                if "not applicable" in text.lower(): return "➖ N/A"
                                return "⚠️ Warning/Fail"
                                
                            r1.metric("Symptom Match", format_status(report.get("symptom_check", "")), help=report.get("symptom_check"))
                            r2.metric("Age Criteria", format_status(report.get("age_check", "")), help=report.get("age_check"))
                            r3.metric("Dosage Limits", format_status(report.get("dosage_check", "")), help=report.get("dosage_check"))
                            
                            if report.get("notes"):
                                st.markdown("#### Detailed Notes")
                                for n in report.get("notes", []):
                                    st.markdown(f"- {n}")
                    except Exception as e:
                        st.error(f"Verification Error: {e}")

    with tab2:
        with st.container(border=True):
            d_med = st.text_input("Search Medication Name", value=default_med, key="d_med")
            if st.button("Fetch Standard Guidelines"):
                with st.spinner("Fetching data..."):
                    try:
                        res = get_dosage(d_med, patient_age_months)
                        st.session_state.app_data['dosage_results'] = res
                        
                        st.markdown(f"### 💊 Guidelines for {res.get('drug_generic', d_med)}")
                        c1, c2 = st.columns(2)
                        c1.metric("Max Daily Dose", f"{res.get('max_daily_dose')} {res.get('max_daily_dose_units')}")
                        c2.metric("Dosing Interval", f"Every {res.get('dosing_interval_hours')} hours")
                        
                        st.warning(f"**Safety Flag:** {res.get('notes_key_safety', 'None listed.')}")
                    except Exception as e:
                        st.error(f"Could not fetch data. (Is the medicine in the database?) {e}")
