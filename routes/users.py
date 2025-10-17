from fastapi import APIRouter, HTTPException, status
from typing import List, Union
from schemas.user import UserCreate, User
from services import user_service

router = APIRouter()

# ----- Single user endpoints ----- #
@router.post("/", response_model=Union[User, List[User]], status_code=201)
def create_user(payload: Union[UserCreate, List[UserCreate]]):
    if isinstance(payload, list):
        return [user_service.create_user(u) for u in payload]
    return user_service.create_user(payload)

@router.get("/", response_model=list[User])
def list_users():
    return user_service.list_users()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, payload: UserCreate):
    updated = user_service.update_user(user_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.post("/{user_id}/deactivate", status_code=status.HTTP_204_NO_CONTENT)
def deactivate(user_id: int):
    ok = user_service.deactivate_user(user_id)
    if not ok:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")


# ----- New batch endpoint ----- #
@router.post("/batch/", response_model=List[User], status_code=status.HTTP_201_CREATED)
def create_users_batch(payload: List[UserCreate]):
    created_users = [user_service.create_user(user) for user in payload]
    return created_users

