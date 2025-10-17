from typing import List, Optional
from schemas.user import UserCreate, User
from .storage import USERS, next_id

def create_user(data: UserCreate) -> User:
    uid = next_id("user")
    user = User(id=uid, name=data.name, email=data.email, is_active=True)
    USERS[uid] = user.model_dump()
    return user

def get_user(user_id: int) -> Optional[User]:
    raw = USERS.get(user_id)
    return User(**raw) if raw else None

def list_users() -> List[User]:
    return [User(**u) for u in USERS.values()]

def update_user(user_id: int, data: UserCreate) -> Optional[User]:
    if user_id not in USERS:
        return None
    USERS[user_id].update(name=data.name, email=data.email)
    return User(**USERS[user_id])

def deactivate_user(user_id: int) -> bool:
    if user_id not in USERS:
        return False
    USERS[user_id]["is_active"] = False
    return True

def delete_user(user_id: int) -> bool:
    return USERS.pop(user_id, None) is not None

