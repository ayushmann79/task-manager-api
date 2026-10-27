from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "Task Manager API is running"


def test_create_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Learn CI/CD"})

    assert response.status_code == 201
    assert response.json["title"] == "Learn CI/CD"
    assert response.json["completed"] is False


def test_empty_title_is_rejected():
    client = app.test_client()
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 400
