import streamlit as st
from api import get_interactions

def render():
    st.title("⚡ Step 3: Drug Interaction Check")
    st.markdown("Leverage AI to analyze potential adverse interactions between multiple prescribed medications.")
    
    ner_meds = st.session_state.app_data.get('ner_results', {}).get('Medication', [])
    med_input = st.text_area("Medications to check (comma-separated):", value=", ".join(ner_meds))
    
    if st.button("Analyze Interactions", type="primary"):
        med_list = [m.strip() for m in med_input.split(",") if m.strip()]
        
        if len(med_list) < 2:
            st.warning("Please enter at least 2 medications to check for interactions.")
        else:
            with st.spinner("AI is analyzing pharmacological data..."):
                try:
                    res = get_interactions(med_list)
                    st.session_state.app_data['interaction_results'] = res
                    
                    with st.container(border=True):
                        st.markdown(res)
                except Exception as e:
                    st.error(f"Interaction Service Error: {e}")
