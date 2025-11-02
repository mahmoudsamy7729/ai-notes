import pytest
from fastapi import status

from app.tests.conftest import TestSessionDB

@pytest.mark.asyncio
async def test_retrieve_notes_unauthorized(client):
    response = await client.get("/notes/")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()["detail"] == "Not authenticated"


@pytest.mark.asyncio
async def test_retrieve_notes_empty(logged_in_user, client):
    token = logged_in_user["token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = await client.get("/notes/", headers= headers)
    assert response.status_code == status.HTTP_200_OK
    assert "notes" in response.json() 
    assert response.json()["notes"] == []
    assert response.json()["message"] == "No notes found."


@pytest.mark.asyncio
async def test_create_note(logged_in_user, client):
    headers = {"Authorization": f"Bearer {logged_in_user["token"]}"}
    response = await client.post("/notes/create", json= {
        "title": "Note test title",
        "content": "This is the content of the test note."
    }, headers= headers)
    assert response.status_code == 201
    assert response.json()["message"] == "Note created successfully"
    assert "note" in response.json()
    assert response.json()["note"]["title"] == "Note test title"