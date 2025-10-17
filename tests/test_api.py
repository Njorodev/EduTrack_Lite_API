from fastapi.testclient import TestClient
from main import app
from services import storage

client = TestClient(app)

def setup_module(module):
    """Reset the in-memory storage before running all tests."""
    storage.USERS.clear()
    storage.COURSES.clear()
    storage.ENROLLMENTS.clear()
    storage._next.update({"user": 1, "course": 1, "enrollment": 1})


#  USER TESTS 

def test_create_users_and_list():
    # create users
    r = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert r.status_code == 201
    # create second user
    r = client.post("/users/", json={"name": "Bob", "email": "bob@example.com"})
    assert r.status_code == 201

    # list users
    r = client.get("/users/")
    assert r.status_code == 200
    users = r.json()
    assert len(users) == 2
    assert users[0]["name"] == "Alice"


def test_get_user_by_id_and_update_user():
    # get user by id
    r = client.get("/users/1")
    assert r.status_code == 200
    assert r.json()["email"] == "alice@example.com"

    # update user
    update = {"name": "Alice Updated", "email": "alice.new@example.com"}
    r = client.put("/users/1", json=update)
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Alice Updated"
    assert data["email"] == "alice.new@example.com"


def test_deactivate_user_and_delete_user():
    # deactivate
    r = client.post("/users/2/deactivate")
    assert r.status_code == 204

    # delete
    r = client.delete("/users/2")
    assert r.status_code == 204

    # confirm deletion
    r = client.get("/users/2")
    assert r.status_code == 404


#  COURSE TESTS 

def test_create_and_list_courses():
    # create courses
    r = client.post("/courses/", json={"title": "Python Basics", "description": "Intro to Python"})
    assert r.status_code == 201
    # create second course
    r = client.post("/courses/", json={"title": "Data Science", "description": "Learn ML"})
    assert r.status_code == 201

    # list courses
    r = client.get("/courses/")
    assert r.status_code == 200
    courses = r.json()
    assert len(courses) >= 2


def test_update_and_close_course():
    # update course
    r = client.put("/courses/1", json={"title": "Python Mastery", "description": "Advanced Python"})
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "Python Mastery"

    # close course
    r = client.post("/courses/2/close")
    assert r.status_code == 204


def test_get_users_in_course_before_enrollment():
    # initially no users enrolled
    r = client.get("/courses/1/users")
    assert r.status_code == 200
    assert r.json() == []


#  ENROLLMENT TESTS 
def test_enroll_user_in_course_and_list_enrollments():
    # enroll user 1 in course 1
    r = client.post("/enrollments/", json={"user_id": 1, "course_id": 1})
    assert r.status_code == 201
    enroll = r.json()
    assert enroll["user_id"] == 1
    assert enroll["course_id"] == 1

    # get all enrollments
    r = client.get("/enrollments/")
    assert r.status_code == 200
    assert len(r.json()) >= 1


def test_cannot_enroll_in_closed_course():
    # enroll user 1 in course 2 (which is closed)
    r = client.post("/enrollments/", json={"user_id": 1, "course_id": 2})
    assert r.status_code == 400


def test_cannot_double_enroll():
    # enroll user 1 in course 1 again
    r = client.post("/enrollments/", json={"user_id": 1, "course_id": 1})
    assert r.status_code == 400


def test_mark_course_complete_and_check_completion():
    # mark enrollment as complete
    r = client.post("/enrollments/1/complete")
    assert r.status_code == 200
    assert r.json()["completed"] is True


def test_get_enrollments_for_user():
    # get enrollments for user 1
    r = client.get("/enrollments/user/1")
    assert r.status_code == 200
    data = r.json()
    assert len(data) >= 1
    assert data[0]["completed"] is True


#  EDGE CASES

def test_mark_nonexistent_enrollment_as_complete():
    # mark nonexistent enrollment as complete
    r = client.post("/enrollments/999/complete")
    assert r.status_code == 404


def test_create_invalid_user_missing_fields():
    # missing email
    r = client.post("/users/", json={"name": "InvalidUser"})
    assert r.status_code in (400, 422)
