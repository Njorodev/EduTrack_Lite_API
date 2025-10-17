from fastapi import APIRouter, HTTPException, status
from schemas.course import CourseCreate, Course
from services import course_service, enrollment_service

router = APIRouter()

@router.post("/", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate):
    return course_service.create_course(payload)

@router.get("/", response_model=list[Course])
def list_courses():
    return course_service.list_courses()

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, payload: CourseCreate):
    updated = course_service.update_course(course_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@router.post("/{course_id}/close", status_code=status.HTTP_204_NO_CONTENT)
def close_enrollment(course_id: int):
    ok = course_service.close_enrollment(course_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Course not found")

@router.get("/{course_id}/users", response_model=list[int])
def users_in_course(course_id: int):
    # Ensure course exists
    course = course_service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return enrollment_service.list_users_in_course(course_id)

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int):
    if not course_service.delete_course(course_id):
        raise HTTPException(status_code=404, detail="Course not found")
