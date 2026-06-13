# Główny plik aplikacji – uruchamia FastAPI, rejestruje routery, middleware, CORS.

from fastapi import FastAPI
from app.database import engine, Base
from app.models import ingredient
from app.routers import ingredients

app = FastAPI()

# Tworzenie tabel w bazie danych
Base.metadata.create_all(bind=engine)

# Rejestracja routerów
app.include_router(ingredients.router)