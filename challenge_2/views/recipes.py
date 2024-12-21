
import streamlit as st
import requests

RECIPES_API_URL = "http://localhost:8000/recipes"

def show():
    st.markdown("### Recipes Management")

    # Fetch and display all recipes
    refresh = st.button("Refresh")
    if refresh:
        response = requests.get(RECIPES_API_URL)
        if response.status_code == 200:
            recipes = response.json()
            st.write(recipes)
        else:
            st.error("Error fetching recipes")

    # Convert text to recipe
    with st.expander("➕ Convert Text to Recipe"):
        with st.form("convert_text_to_recipe"):
            text = st.text_area("Recipe Text")
            submitted = st.form_submit_button("Convert")
            if submitted:
                response = requests.post(f"{RECIPES_API_URL}/convert", json={"text": text})
                if response.status_code == 200:
                    st.success("Recipe converted successfully. Refresh the page to see changes")
                else:
                    st.error("Error converting text to recipe")