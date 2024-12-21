import streamlit as st
import requests

API_URL = "http://localhost:8000/ingredients"

def fetch_ingredients():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching ingredients")
        return []

def show():
    st.markdown("### Ingredients Management")

    # Fetch and display all ingredients
    refresh = st.button("Refresh")
    ingredients = fetch_ingredients()
    if ingredients:
        st.table([{
            "ID": ingredient['id'],
            "Name": ingredient['name'],
            "Quantity": f"{ingredient['quantity']} {ingredient['unit']}",
            "Calories": ingredient['calories'],
            "Category": ingredient['category']
        } for ingredient in ingredients])
    else:
        st.write("No ingredients found")

    # Create Ingredient
    with st.expander("➕ Add Ingredient"):
        with st.form("create_ingredient"):
            name = st.text_input("Name")
            quantity = st.text_input("Quantity")
            unit = st.text_input("Unit")
            calories = st.number_input("Calories", min_value=0)
            category = st.text_input("Category")
            submitted = st.form_submit_button("Create")
            if submitted:
                response = requests.post(API_URL, json={
                    "name": name,
                    "quantity": quantity,
                    "unit": unit,
                    "calories": calories,
                    "category": category
                })
                if response.status_code == 200:
                    st.success("Ingredient created successfully. Refresh the page to see changes")
                else:
                    st.error("Error creating ingredient")

    # Edit Ingredient
    with st.expander("✏️ Edit Ingredient"):
        edit_id = st.number_input("Enter Ingredient ID to Edit", min_value=1, step=1)
        if st.button("Load Ingredient"):
            response = requests.get(f"{API_URL}/{edit_id}")
            if response.status_code == 200:
                ingredient = response.json()
                st.session_state.edit_ingredient = ingredient
            else:
                st.error("Ingredient not found")

        if 'edit_ingredient' in st.session_state:
            ingredient = st.session_state.edit_ingredient
            with st.form("update_ingredient"):
                name = st.text_input("Name", value=ingredient['name'])
                quantity = st.text_input("Quantity", value=ingredient['quantity'])
                unit = st.text_input("Unit", value=ingredient['unit'])
                calories = st.number_input("Calories", min_value=0, value=ingredient['calories'])
                category = st.text_input("Category", value=ingredient['category'])
                submitted = st.form_submit_button("Update")
                if submitted:
                    response = requests.put(f"{API_URL}/{edit_id}", json={
                        "name": name,
                        "quantity": quantity,
                        "unit": unit,
                        "calories": calories,
                        "category": category
                    })
                    if response.status_code == 200:
                        st.success("Ingredient updated successfully. Refresh the page to see changes")
                        del st.session_state.edit_ingredient
                    else:
                        st.error("Error updating ingredient")

    # Delete Ingredient
    with st.expander("🗑️ Delete Ingredient"):
        delete_id = st.number_input("Enter Ingredient ID to Delete", min_value=1, step=1)
        if st.button("Delete"):
            response = requests.delete(f"{API_URL}/{delete_id}")
            if response.status_code == 200:
                st.success("Ingredient deleted successfully. Refresh the page to see changes")
            else:
                st.error("Error deleting ingredient")