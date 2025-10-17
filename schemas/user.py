from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr

class User(UserCreate):
    id: int
    is_active: bool = True
