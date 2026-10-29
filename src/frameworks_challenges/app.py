from typing import Annotated

from fastapi import APIRouter, Body

from libs.commans.models.user import UserPostRequest, UserPostResponse

app = APIRouter()


@app.post("/user", response_model=UserPostResponse)
def insert_user(users: Annotated[UserPostRequest, Body()]):
    metadata = {}
    if users.gender:
        metadata["gender"] = users.gender 
    if users.education:
        metadata["education"] = users.education
    
    response = UserPostResponse(
        name=users.first_name + users.last_name,
        metadata=metadata
    )
    return response
