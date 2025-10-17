
# 🎓 EduTrack Lite API

**AltSchool of Backend Engineering – Baraka 2025 Second Semester Examination Project (Python)**  
*Instructor: Backend Engineering Faculty | Month [4]*  

---

## 📘 Project Overview

**EduTrack Lite API** is a lightweight academic tracking system that allows users to:

- Register for courses
- Manage course information
- Track course enrollments and completion status  

It provides **CRUD operations** for `Users`, `Courses`, and `Enrollments` with simple validation and relationship logic — implemented using **FastAPI**, **Pydantic**, and **modular Python structure**.

---

## 🧩 Entities

### 👤 User

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique identifier |
| `name` | str | Full name |
| `email` | str | Email address |
| `is_active` | bool | Whether the user is active (default: `True`) |

---

### 📚 Course

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique identifier |
| `title` | str | Course name |
| `description` | str | Brief description |
| `is_open` | bool | Whether the course is open for enrollment (default: `True`) |

### 📝 Enrollment

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique identifier |
| `user_id` | int | ID of the enrolling user |
| `course_id` | int | ID of the course |
| `enrolled_date` | str | Date of enrollment |
| `completed` | bool | Course completion status (default: `False`) |
| `enrolled_date` | str | Date of enrollment |
| `completed` | bool | Course completion status (default: `False`) |

---

## ⚙️ Technical Requirements

✅ **Pydantic** models for validation  
✅ **In-memory data storage** (using Python dictionaries)  
✅ **Modular architecture**:  

``` text

EduTrack_Lite_API/
│
├── main.py
├── routes/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── schemas/
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
├── services/
│   ├── user_service.py
│   ├── course_service.py
│   └── enrollment_service.py
├── storage.py
└── tests/
    └── test_api.py

````

✅ **Appropriate HTTP status codes**  
✅ **Unit tests** for all endpoints using `pytest`  
✅ **No authentication required**  

---

## 🚀 Getting Started

### 🧱 Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Njorodev/AltSchool-attendance/tree/main/Semester_2/EduTrack_Lite_API.git
cd EduTrack_Lite_API

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate     # (Linux/macOS)
venv\Scripts\activate        # (Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the FastAPI application
uvicorn main:app --reload
````

### 🧪 Run Tests

```bash
PYTHONPATH=. pytest -q
or
PYTHONPATH=. pytest -v -ra
```

✅ All tests should pass:

``` text
collected 13 items                                                                     

tests/test_api.py::test_create_users_and_list PASSED                             [  7%]
tests/test_api.py::test_get_user_by_id_and_update_user PASSED                    [ 15%]
tests/test_api.py::test_deactivate_user_and_delete_user PASSED                   [ 23%]
tests/test_api.py::test_create_and_list_courses PASSED                           [ 30%]
tests/test_api.py::test_update_and_close_course PASSED                           [ 38%]
tests/test_api.py::test_get_users_in_course_before_enrollment PASSED             [ 46%]
tests/test_api.py::test_enroll_user_in_course_and_list_enrollments PASSED        [ 53%]
tests/test_api.py::test_cannot_enroll_in_closed_course PASSED                    [ 61%]
tests/test_api.py::test_cannot_double_enroll PASSED                              [ 69%]
tests/test_api.py::test_mark_course_complete_and_check_completion PASSED         [ 76%]
tests/test_api.py::test_get_enrollments_for_user PASSED                          [ 84%]
tests/test_api.py::test_mark_nonexistent_enrollment_as_complete PASSED           [ 92%]
tests/test_api.py::test_create_invalid_user_missing_fields PASSED                [100%]

================================== 13 passed in 0.48s ==================================
```

---

### 👤 **User Endpoints**

| Method   | Endpoint                      | Description                   |
| -------- | ----------------------------- | ----------------------------- |
| `GET`    | `/users/`                     | List all users                |
| `POST`   | `/users/`                     | Create a new user             |
| `POST`   | `/users/batch/`               | Create multiple users at once |
| `GET`    | `/users/{user_id}`            | Get user by ID                |
| `PUT`    | `/users/{user_id}`            | Update user                   |
| `DELETE` | `/users/{user_id}`            | Delete user                   |
| `POST`   | `/users/{user_id}/deactivate` | Deactivate user               |
| `PUT`    | `/users/{user_id}`            | Update user                   |
| `DELETE` | `/users/{user_id}`            | Delete user                   |
| `POST`   | `/users/{user_id}/deactivate` | Deactivate user               |

### 🗓️ **Course Endpoints**

| Method   | Endpoint                     | Description                         |
| -------- | ---------------------------- | ----------------------------------- |
| `GET`    | `/courses/`                  | List all courses                    |
| `POST`   | `/courses/`                  | Create new course                   |
| `GET`    | `/courses/{course_id}`       | Get course by ID                    |
| `PUT`    | `/courses/{course_id}`       | Update course                       |
| `DELETE` | `/courses/{course_id}`       | Delete course                       |
| `POST`   | `/courses/{course_id}/close` | Close enrollment                    |
| `GET`    | `/courses/{course_id}/users` | List all users enrolled in a course |
| `DELETE` | `/courses/{course_id}`       | Delete course                       |
| `POST`   | `/courses/{course_id}/close` | Close enrollment                    |
| `GET`    | `/courses/{course_id}/users` | List all users enrolled in a course |

### 📝 **Enrollment Endpoints**

| Method | Endpoint                            | Description                          |
| ------ | ----------------------------------- | ------------------------------------ |
| `GET`  | `/enrollments/`                     | List all enrollments                 |
| `POST` | `/enrollments/`                     | Enroll a user in a course            |
| `GET`  | `/enrollments/user/{user_id}`       | View enrollments for a specific user |
| `POST` | `/enrollments/{enroll_id}/complete` | Mark a course as completed           |
| `POST` | `/enrollments/`                     | Enroll a user in a course            |
| `GET`  | `/enrollments/user/{user_id}`       | View enrollments for a specific user |
| `POST` | `/enrollments/{enroll_id}/complete` | Mark a course as completed           |

**Rules:**

- Only **active users** can enroll.
- Course must be **open**.
- A user **cannot enroll twice** in the same course.

---

## 📊 Example Data

```json
{
  "course": {
    "id": 1,
    "title": "Python Basics",
    "description": "Learn Python fundamentals",
    "is_open": true
  },
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "is_active": true
  },
  "enrollment": {
    "id": 1,
    "user_id": 1,
    "course_id": 1,
    "enrolled_date": "2025-09-16",
    "completed": false
  }
}
```

---

## 🌐 Interactive API Docs

After running the app, visit:

- Swagger UI → **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
- ReDoc → **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

---

## 🧠 Notes

- Keep user creation simple (no password/auth required).
- Data resets every time the server restarts (in-memory storage).
- Follows RESTful standards with clear response models and error handling.

---

## 🧩 Version

**EduTrack Lite API v0.1.0**
**OpenAPI 3.1 Specification**

---

## 🔬️ In action

*[**FrontEnd**](https://njorodev.github.io/AltSchool-attendance/Semester_2/EduTrack-Frontend/index.html)
*[**BackEnd**](https://edu-track-api.onrender.com/docs)

## 👨‍💻 Author

**Frank Njoroge**
AltSchool of Backend Engineering – Baraka 2025
GitHub: [@frank-njoroge](https://github.com/Njorodev)

---
