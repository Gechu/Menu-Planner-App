from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/random-meal")
def random_meal():
    meals = ["Pizza", "Curry", "Tacos", "Sałatka"]
    return {"meal": random.choice(meals)}