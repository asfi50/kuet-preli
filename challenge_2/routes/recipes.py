from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from text_to_recipe import convert_to_recipe

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/convert")
async def convert_text_to_recipe(request: TextRequest):
    try:
        text = request.text
        recipe = convert_to_recipe(text)
        # append this recipe as text in my_fav_recipes.txt
        with open("my_fav_recipes.txt", "a") as f:
            f.write(str(recipe.model_dump())+"\n")
        return recipe
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# get all recipes from my_fav_recipes.txt
@router.get("/")
async def get_my_fav_recipes():
    with open("my_fav_recipes.txt", "r") as f:
        recipes = f.readlines()
    return recipes



