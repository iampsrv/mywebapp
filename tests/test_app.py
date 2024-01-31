import pytest
from app import app as flask_app, todos

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_add_todo(client):
    # Simulate posting a new todo item
    response = client.post('/add', data={'todo_item': 'Test Todo'})
    assert response.status_code == 302  # Redirect status
    # Check if the todo is added
    assert 'Test Todo' in todos.values()

def test_remove_todo(client):
    # Add a todo item first
    client.post('/add', data={'todo_item': 'Test Todo'})
    todo_id = list(todos.keys())[0]

    # Simulate removing the todo item
    response = client.get(f'/remove/{todo_id}')
    assert response.status_code == 302  # Redirect status
    # Check if the todo is removed
    assert todo_id not in todos
