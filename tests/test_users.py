import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import json
import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"User Management System" in res.data

def test_create_user(client):
    payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "securepass"
    }
    res = client.post("/users", json=payload)
    assert res.status_code == 201 or res.status_code == 200
    assert b"User created" in res.data

def test_get_all_users(client):
    res = client.get("/users")
    assert res.status_code == 200
    assert isinstance(res.json, list) or b"[" in res.data

def test_login_success(client):
    # Assuming user was created before
    res = client.post("/login", json={
        "email": "john@example.com",
        "password": "securepass"
    })
    assert res.status_code == 200
    assert res.json["status"] == "success"

def test_login_fail(client):
    res = client.post("/login", json={
        "email": "wrong@example.com",
        "password": "badpass"
    })
    assert res.status_code == 401
    assert res.json["status"] == "failed"
