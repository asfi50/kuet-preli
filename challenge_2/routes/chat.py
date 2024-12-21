from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from suggest_recipe import suggest
from database import get_connection

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

# Dependency to get database connection
def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

@router.post("/suggest")
async def suggest_recipe_route(request: ChatRequest, db=Depends(get_db)):
    try:
        prompt = request.prompt
        cursor = db.cursor()
        cursor.execute("SELECT name FROM ingredients")
        ingredients = [row["name"] for row in cursor.fetchall()]

        with open("my_fav_recipes.txt", "r") as file:
            favorite_recipes = file.read()

        recipe_suggestion = suggest(prompt, ingredients, favorite_recipes)
        return {"suggested_recipe": recipe_suggestion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))