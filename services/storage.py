from typing import Dict, Any
from datetime import date

USERS: Dict[int, Dict[str, Any]] = {}
COURSES: Dict[int, Dict[str, Any]] = {}
ENROLLMENTS: Dict[int, Dict[str, Any]] = {}

_next = {"user": 1, "course": 1, "enrollment": 1}

def next_id(kind: str) -> int:
    val = _next[kind]
    _next[kind] += 1
    return val
