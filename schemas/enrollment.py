from pydantic import BaseModel
from datetime import date
from typing import Optional

class EnrollmentCreate(BaseModel):
    user_id: int
    course_id: int

class Enrollment(BaseModel):
    id: int
    user_id: int
    course_id: int
    enrolled_date: date
    completed: bool = False
