from typing import List, Optional
from datetime import date
from schemas.enrollment import EnrollmentCreate, Enrollment
from .storage import ENROLLMENTS, USERS, COURSES, next_id

def create_enrollment(data: EnrollmentCreate) -> Enrollment:
    # Validation checks are expected to be done before calling this in routes,
    # but we keep a minimal guard here.
    eid = next_id("enrollment")
    e = Enrollment(id=eid, user_id=data.user_id, course_id=data.course_id, enrolled_date=date.today(), completed=False)
    ENROLLMENTS[eid] = e.model_dump()
    return e

def get_enrollment(enroll_id: int) -> Optional[Enrollment]:
    raw = ENROLLMENTS.get(enroll_id)
    return Enrollment(**raw) if raw else None

def list_enrollments() -> List[Enrollment]:
    return [Enrollment(**e) for e in ENROLLMENTS.values()]

def list_enrollments_for_user(user_id: int) -> List[Enrollment]:
    return [Enrollment(**e) for e in ENROLLMENTS.values() if e["user_id"] == user_id]

def list_users_in_course(course_id: int) -> List[int]:
    return [e["user_id"] for e in ENROLLMENTS.values() if e["course_id"] == course_id]

def mark_completed(enroll_id: int) -> Optional[Enrollment]:
    if enroll_id not in ENROLLMENTS:
        return None
    ENROLLMENTS[enroll_id]["completed"] = True
    return Enrollment(**ENROLLMENTS[enroll_id])

def user_already_enrolled(user_id: int, course_id: int) -> bool:
    return any(e for e in ENROLLMENTS.values() if e["user_id"] == user_id and e["course_id"] == course_id)
