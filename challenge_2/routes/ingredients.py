from fastapi import APIRouter, HTTPException, Depends
from models import IngredientBase
from database import get_connection
import sqlite3

router = APIRouter()

class IngredientCreate(IngredientBase):
    pass

class Ingredient(IngredientBase):
    id: int

# Dependency to get database connection
def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()

# Routes
@router.get("/", response_model=list[Ingredient])
def read_ingredients(skip: int = 0, limit: int = 10, name: str = "", db=Depends(get_db)):
    cursor = db.cursor()
    if name:
        cursor.execute("SELECT * FROM ingredients WHERE name LIKE ? LIMIT ? OFFSET ?", (f"%{name}%", limit, skip))
    else:
        cursor.execute("SELECT * FROM ingredients LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

@router.get("/{ingredient_id}", response_model=Ingredient)
def read_ingredient(ingredient_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ingredients WHERE id = ?", (ingredient_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return dict(row)

@router.post("/", response_model=Ingredient)
def create_ingredient(ingredient: IngredientCreate, db=Depends(get_db)):
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO ingredients (name, quantity, unit, calories, category) VALUES (?, ?, ?, ?, ?)", 
                       (ingredient.name, ingredient.quantity, ingredient.unit, ingredient.calories, ingredient.category))
        db.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Ingredient already exists")
    ingredient_id = cursor.lastrowid
    cursor.execute("SELECT * FROM ingredients WHERE id = ?", (ingredient_id,))
    return dict(cursor.fetchone())

@router.put("/{ingredient_id}", response_model=Ingredient)
def update_ingredient(ingredient_id: int, ingredient: IngredientCreate, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("UPDATE ingredients SET name = ?, quantity = ?, unit = ?, calories = ?, category = ? WHERE id = ?", 
                   (ingredient.name, ingredient.quantity, ingredient.unit, ingredient.calories, ingredient.category, ingredient_id))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    cursor.execute("SELECT * FROM ingredients WHERE id = ?", (ingredient_id,))
    return dict(cursor.fetchone())

@router.delete("/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM ingredients WHERE id = ?", (ingredient_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"detail": "Ingredient deleted successfully"}
