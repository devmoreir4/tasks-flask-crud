import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    url = f'{BASE_URL}/tasks'

    new_task_data = {
        'title': 'Task 1',
        'description': 'Task 1 description'
    }

    response = requests.post(url, json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    url = f'{BASE_URL}/tasks'
    response = requests.get(url)
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    task_id = tasks[0]
    url = f'{BASE_URL}/tasks/{task_id}'
    response = requests.get(url)
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        url = f'{BASE_URL}/tasks/{task_id}'
        payload = {
            "completed": True,
            "description": "New description updated",
            "title": "New title updated"
        }
        response = requests.put(url, json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa especifica
        response = requests.get(url)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]
        assert response_json["completed"] == payload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        url = f'{BASE_URL}/tasks/{task_id}'
        response = requests.delete(url)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Verificar se a tarefa foi deletada
        response = requests.get(url)
        assert response.status_code == 404

