from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    #events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@email.com",
                "username": "Username_example",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@email.com",
                "password": "user_strong_password"
            }
        }