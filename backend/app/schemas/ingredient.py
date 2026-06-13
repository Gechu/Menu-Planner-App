from pydantic import BaseModel

# Schematy Pydantic dla składników – definiują strukturę danych dla tworzenia i aktualizacji składników.
class IngredientCreate(BaseModel):
    name: str
    category: str
