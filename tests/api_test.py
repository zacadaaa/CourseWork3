import pytest
from app import app

def test_api():

    response = app.test_client().get('/api/posts')
    assert response.json.get("poster_name") == "leo", "Имя получено верно"