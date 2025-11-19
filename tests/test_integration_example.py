import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # add project root
import pytest
from app import app, items


@pytest.fixture(autouse=True)
def clear_items():
    """Ensure the in-memory list is clean before each test."""
    items.clear()
    yield
    items.clear()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_route(client):
    resp = client.get("/")
    assert resp.status_code == 200


def test_add_item_route(client):
    resp = client.post("/add", data={"item": "Milk"}, follow_redirects=True)
    assert resp.status_code == 200
    assert items == ["Milk"]
    assert "Milk" in resp.get_data(as_text=True)


def test_delete_item_route(client):
    items.extend(["A", "B"])
    resp = client.get("/delete/0", follow_redirects=True)
    assert resp.status_code == 200
    assert items == ["B"]


def test_update_item_route(client):
    items.append("Old")
    resp = client.post(
        "/update/0", data={"new_item": "New"}, follow_redirects=True
    )
    assert resp.status_code == 200
    assert items == ["New"]
