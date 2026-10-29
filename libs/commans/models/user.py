from pydantic import BaseModel


class UserPostRequest(BaseModel):
    first_name: str
    last_name: str
    gender: str | None
    education: str | None


class UserPostResponse(BaseModel):
    name: str
    metadata: dict | None
