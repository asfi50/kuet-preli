from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import base64, httpx
from langchain.output_parsers import PydanticOutputParser
from models import RecipeBase
import os

# Define the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY") or "AIzaSyBA9Az08B5dFYEEItqjq3SXPJOpnPHj1GQ")


def convert_to_recipe(text): 

    parser = PydanticOutputParser(pydantic_object=RecipeBase)
    format_instructions = parser.get_format_instructions()

    message = HumanMessage(
    content=[
        {"type": "text", "text": f"convert this {text} into a recipe of this format. \n'{format_instructions}'\n"},
        ],
    )

    response = model.invoke([message])

    if parser is None:
        return response.content
    
    return parser.parse(response.content)



if __name__ == '__main__':
    recipe = convert_to_recipe("1 cup of flour, 2 eggs, 3 cups of sugar, 4 cups of milk, 5 cups of water")
    print(recipe)


