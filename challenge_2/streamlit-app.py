import streamlit as st
from streamlit_option_menu import option_menu
from views import ingredients, recipes, chat

st.title("Recipe Recommendation App")

with st.sidebar:
    menu = option_menu(
        menu_title='Menu',
        options=["Ingredients", "Recipes", "Chat", "Help"],
        default_index=0,
    )

if menu == "Ingredients":
    ingredients.show()
elif menu == "Recipes":
    recipes.show()
elif menu == "Chat":
    chat.show()



