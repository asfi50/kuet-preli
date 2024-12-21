from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import base64, httpx
from langchain.output_parsers import PydanticOutputParser
import os

# Define the model
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", api_key=os.getenv("GOOGLE_API_KEY") or "AIzaSyBA9Az08B5dFYEEItqjq3SXPJOpnPHj1GQ")


def extract_text(path, parser=None):
    with open(path, "rb") as image_file:
        image = image_file.read()
    image_data = base64.b64encode(image).decode('utf-8')
    
    if parser is None:
        format_instructions = "give the data in plain text"
    else :
        format_instructions = parser.get_format_instructions()

    message = HumanMessage(
    content=[
        {"type": "text", "text": f"ocr this image accurately and extract text. just give me the text, nothing else. do not alter any word \n'{format_instructions}'\n"},
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
        },
        ],
    )

    response = model.invoke([message])

    if parser is None:
        return response.content
    
    return parser.parse(response.content)


