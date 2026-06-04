from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class UserInput(BaseModel):
    age: int = Field(gt=0, lt=120)


@app.get("/")
def home():
    return {
        "message": "Age Classifier API"
    }


@app.post("/predict")
def predict(data: UserInput):

    if data.age <= 17:
        category = "Child"

    elif data.age <= 59:
        category = "Adult"

    else:
        category = "Senior Citizen"

    return {
        "age": data.age,
        "category": category
    }