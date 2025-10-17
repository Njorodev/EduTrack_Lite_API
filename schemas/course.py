from pydantic import BaseModel, Field
from typing import Optional

class CourseCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = ""

class Course(CourseCreate):
    id: int
    is_open: bool = True
