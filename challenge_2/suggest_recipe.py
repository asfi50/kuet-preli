from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import base64, httpx
from langchain.output_parsers import PydanticOutputParser
from models import RecipeBase
import os

# Define the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY") or "AIzaSyBA9Az08B5dFYEEItqjq3SXPJOpnPHj1GQ")


def suggest(prompt, ingredients, favorite_recipes):
    message = HumanMessage(
    content=[
        {"type": "text", "text": f"suggest a recipe for this prompt: {prompt} using these ingredients: {ingredients} and these favorite recipes: {favorite_recipes} \n\n\n it will be good if the recipe is from the favorite recipes\n"},
        ],
    )

    response = model.invoke([message])
    return response.content