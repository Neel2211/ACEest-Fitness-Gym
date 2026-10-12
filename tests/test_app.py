import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_programs():
    client = app.test_client()
    response = client.get("/programs")
    assert response.status_code == 200


def test_add_client():
    client = app.test_client()

    response = client.post(
        "/clients",
        json={
            "name": "Neel",
            "age": 25
        }
    )

    assert response.status_code == 201


def test_get_client():
    client = app.test_client()

    client.post(
        "/clients",
        json={
            "name": "Amit",
            "age": 30
        }
    )

    response = client.get("/clients/Amit")

    assert response.status_code == 200


def test_membership():
    client = app.test_client()

    response = client.get("/membership/Neel")

    assert response.status_code == 200


def test_generate_program():
    client = app.test_client()

    response = client.post("/generate_program/Neel")

    assert response.status_code == 200


def test_add_workout():
    client = app.test_client()

    response = client.post(
        "/workouts",
        json={
            "client": "Neel",
            "workout_type": "Cardio",
            "duration": 45
        }
    )

    assert response.status_code == 201


def test_get_workouts():
    client = app.test_client()

    client.post(
        "/workouts",
        json={
            "client": "Neel",
            "workout_type": "Strength",
            "duration": 60
        }
    )

    response = client.get("/workouts/Neel")

    assert response.status_code == 200
