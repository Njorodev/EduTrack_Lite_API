from fastapi import APIRouter, HTTPException, status
from schemas.enrollment import EnrollmentCreate, Enrollment
from services import enrollment_service, user_service, course_service

router = APIRouter()

@router.post("/", response_model=Enrollment, status_code=status.HTTP_201_CREATED)
def enroll(payload: EnrollmentCreate):
    user = user_service.get_user(payload.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="User is not active")

    course = course_service.get_course(payload.course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    if not course.is_open:
        raise HTTPException(status_code=400, detail="Course enrollment is closed")

    if enrollment_service.user_already_enrolled(payload.user_id, payload.course_id):
        raise HTTPException(status_code=400, detail="User already enrolled in this course")

    return enrollment_service.create_enrollment(payload)

@router.get("/", response_model=list[Enrollment])
def list_all_enrollments():
    return enrollment_service.list_enrollments()

@router.get("/user/{user_id}", response_model=list[Enrollment])
def enrollments_for_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return enrollment_service.list_enrollments_for_user(user_id)

@router.post("/{enroll_id}/complete", response_model=Enrollment)
def mark_complete(enroll_id: int):
    e = enrollment_service.mark_completed(enroll_id)
    if not e:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return e
