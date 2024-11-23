import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    data = {
        'title': 'Test',
        'description': 'Task for test'
    }
    response = requests.post(f'{BASE_URL}/tasks', json=data)
    assert response.status_code == 201
    task = response.json()
    assert "message" in task
    assert "id" in task
    tasks.append(task["id"])