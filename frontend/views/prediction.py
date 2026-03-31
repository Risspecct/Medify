import streamlit as st
from api import predict_disease

def render():
    st.title("🩺 Step 2: Disease Prediction")
    st.markdown("Medify uses a machine learning model to predict potential diseases based on symptoms.")
    
    # Pre-fill from NER
    ner_symps = st.session_state.app_data.get('ner_results', {}).get('Symptoms', [])
    default_symps = ", ".join(ner_symps)
    
    with st.container(border=True):
        symptoms_input = st.text_input("Enter symptoms (comma-separated):", value=default_symps)
        
        if st.button("Analyze Symptoms", type="primary"):
            symptom_list = [s.strip().lower() for s in symptoms_input.split(",") if s.strip()]
            
            if not symptom_list:
                st.warning("Please enter at least one symptom.")
            else:
                with st.spinner("Running prediction model..."):
                    try:
                        res = predict_disease(symptom_list)
                        preds = res.get("predictions", [])
                        st.session_state.app_data['prediction_results'] = preds
                        
                        if preds:
                            st.write("### Analysis Results")
                            for p in preds:
                                # Convert percentage string to float for progress bar
                                prob_float = float(p['probability'].strip('%')) / 100
                                
                                st.markdown(f"**{p['disease'].title().replace('_', ' ')}**")
                                cols = st.columns([0.8, 0.2])
                                with cols[0]:
                                    st.progress(prob_float)
                                with cols[1]:
                                    st.markdown(f"<h4 style='margin:0; color:#0f766e;'>{p['probability']}</h4>", unsafe_allow_html=True)
                                st.caption(f"Confidence Level: **{p['confidence']}**")
                                st.write("---")
                        else:
                            st.info("No strong predictions found for the given symptoms.")
                    except Exception as e:
                        st.error(f"Prediction Error: {e}")
