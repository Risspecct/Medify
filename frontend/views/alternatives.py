import streamlit as st
from api import get_alternatives

def render():
    st.title("💸 Step 5: Cost & Alternatives")
    st.markdown("Find generic alternatives to save money, and view established home remedies.")
    
    ner = st.session_state.app_data.get('ner_results', {})
    default_med = ner.get('Medication', [""])[0] if ner.get('Medication') else ""
    
    a_med = st.text_input("Medication Name", value=default_med)
    
    if st.button("Find Alternatives & Remedies", type="primary"):
        with st.spinner("Searching knowledge base..."):
            try:
                res = get_alternatives(a_med)
                if not res:
                    st.warning("No alternatives or remedies found for this medication in our current database.")
                else:
                    st.session_state.app_data['alt_results'] = res
                    base_price = res.get('price_in_inr', 0)
                    
                    with st.container(border=True):
                        st.markdown(f"## {a_med.title()}")
                        st.caption(res.get('description', ''))
                        st.metric("Base Price", f"₹{base_price}")
                        st.write("---")
                        
                        col_alt, col_rem = st.columns(2)
                        
                        with col_alt:
                            st.markdown("#### 💊 Cheaper Alternatives")
                            alts = res.get('alternatives', [])
                            if not alts:
                                st.info("No generic alternatives listed.")
                            for alt in alts:
                                with st.expander(f"**{alt['name']}**"):
                                    c1, c2 = st.columns(2)
                                    c1.metric("Price", f"₹{alt['price_in_inr']}")
                                    c2.metric("Savings", f"{alt['savings_percentage']}%", delta=f"{alt['savings_percentage']}%")
                        
                        with col_rem:
                            st.markdown("#### 🌿 Home Remedies")
                            rems = res.get('home_remedies_for_common_uses', {})
                            if not rems:
                                st.info("No home remedies listed.")
                            for cond, rem in rems.items():
                                st.markdown(f"**{cond}:** {rem}")
                                
                    if res.get('notes'):
                        st.info(f"**Important Notes:** {res['notes']}")
                        
            except Exception as e:
                st.error(f"API Error: {e}")
