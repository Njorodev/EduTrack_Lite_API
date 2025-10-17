from typing import List, Optional
from schemas.course import CourseCreate, Course
from .storage import COURSES, next_id

def create_course(data: CourseCreate) -> Course:
    cid = next_id("course")
    course = Course(id=cid, title=data.title, description=data.description or "", is_open=True)
    COURSES[cid] = course.model_dump()
    return course

def get_course(course_id: int) -> Optional[Course]:
    raw = COURSES.get(course_id)
    return Course(**raw) if raw else None

def list_courses() -> List[Course]:
    return [Course(**c) for c in COURSES.values()]

def update_course(course_id: int, data: CourseCreate) -> Optional[Course]:
    if course_id not in COURSES:
        return None
    COURSES[course_id].update(title=data.title, description=data.description or "")
    return Course(**COURSES[course_id])

def close_enrollment(course_id: int) -> bool:
    if course_id not in COURSES:
        return False
    COURSES[course_id]["is_open"] = False
    return True

def delete_course(course_id: int) -> bool:
    return COURSES.pop(course_id, None) is not None
