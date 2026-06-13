from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

@router.post("/")
def create_ingredient(ingredient: IngredientCreate, db: Session = Depends(get_db)):
    db_ingredient = Ingredient(
        name=ingredient.name,
        category=ingredient.category
    )
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient