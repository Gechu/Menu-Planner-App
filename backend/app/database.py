# Konfiguracja połączenia z bazą danych (SQLite) oraz funkcje pomocnicze do zarządzania bazą danych.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ścieżka do bazy danych SQLite
DATABASE_URL = "sqlite:///./app/db.db"

# Silnik bazy danych
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fabryka sesji
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bazowa klasa dla modeli
Base = declarative_base()


# Funkcja pomocnicza do uzyskiwania sesji bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()