from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

# Request Model

class Food(BaseModel):
    name:str
    price:float
    available:bool=True

foods={}
next_id=1

# CREATE
@app.post("/foods", status_code=201)
def create_food(food: Food):
    global next_id

    foods[next_id] = {
        "id": next_id,
        **food.model_dump()
    }

    created_food = foods[next_id]
    next_id += 1

    return created_food


# READ ALL
@app.get("/foods")
def get_foods():
    return list(foods.values())


# READ ONE
@app.get("/foods/{food_id}")
def get_food(food_id: int):
    if food_id not in foods:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    return foods[food_id]


# UPDATE
@app.put("/foods/{food_id}")
def update_food(food_id: int, food: Food):
    if food_id not in foods:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    foods[food_id] = {
        "id": food_id,
        **food.model_dump()
    }

    return foods[food_id]


# DELETE
@app.delete("/foods/{food_id}")
def delete_food(food_id: int):
    if food_id not in foods:
        raise HTTPException(
            status_code=404,
            detail="Food not found"
        )

    deleted_food = foods.pop(food_id)

    return {
        "message": "Food deleted successfully",
        "food": deleted_food
    }
