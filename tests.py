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

def test_get_tasks():
    response = requests.get(f'{BASE_URL}/tasks')
    assert response.status_code == 200
    tasks_data = response.json()
    assert "tasks" in tasks_data
    assert "total_tasks" in tasks_data

def test_get_task():
    response = requests.get(f'{BASE_URL}/tasks/{tasks[0]}')
    assert response.status_code == 200
    task_data = response.json()
    assert "id" in task_data

def test_update_task():
    if tasks:
        data = {
            'title': 'Updated Test',
            'description': 'Updated task for test',
            'completed': True
        }
        response = requests.put(f'{BASE_URL}/tasks/{tasks[0]}', json=data)
        assert response.status_code == 200
        updated_task_data = response.json()
        assert updated_task_data["title"] == "Updated Test"

def test_delete_task():
    if tasks:
        response = requests.delete(f'{BASE_URL}/tasks/{tasks[0]}')
        assert response.status_code == 200
        deleted_task_data = response.json()
        assert deleted_task_data["message"] == "Task deleted successfully"