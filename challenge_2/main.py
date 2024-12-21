from fastapi import FastAPI
from routes import ingredients, recipes, chat
from database import init_db
import dotenv
dotenv.load_dotenv()

# Initialize SQLite database
init_db()

app = FastAPI()

# Include the ingredients router
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

