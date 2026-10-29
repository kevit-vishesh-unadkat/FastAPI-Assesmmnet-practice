from fastapi.testclient import TestClient

from main import main

client = TestClient(app=main)


def test_post_user_complete():
    response = client.post(
        "/user",
        json={
            "first_name": "prit",
            "last_name": "kanani",
            "gender": "male",
            "education": "12+",
        },
    )
    assert response.status_code == 200


def test_post_user_missing_required_field():
    response = client.post(
        "/user",
        json={
            "first_name": "prit",
            "gender": "male",
            "education": "12+",
        },
    )
    assert response.status_code == 422


def test_post_user_uncompatible_datatype():
    response = client.post(
        "/user",
        json={
            "first_name": "prit",
            "last_name": "kanani",
            "gender": "male",
            "education": 12,
        },
    )
    assert response.status_code == 422
