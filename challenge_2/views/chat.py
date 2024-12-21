
import streamlit as st
import requests

CHAT_API_URL = "http://localhost:8000/chat"

def show():
    st.markdown("### Chat Suggestions")

    # Suggest recipe based on prompt
    with st.expander("💬 Suggest Recipe"):
        with st.form("suggest_recipe"):
            prompt = st.text_area("Prompt")
            submitted = st.form_submit_button("Suggest")
            if submitted:
                response = requests.post(f"{CHAT_API_URL}/suggest", json={"prompt": prompt})
                if response.status_code == 200:
                    suggestion = response.json().get("suggested_recipe")
                    st.write(suggestion)
                else:
                    st.error("Error suggesting recipe")