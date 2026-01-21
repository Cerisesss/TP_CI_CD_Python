import os
import tempfile
from app.api import create_app
from app.db import init_db

def test_create_and_get_user():
    db_fd, db_path = tempfile.mkstemp()
    os.environ["APP_DB_PATH"] = db_path

    init_db()
    app = create_app()
    client = app.test_client()

    resp = client.post("/users", json={"name": "bob"})
    assert resp.status_code == 201

    user_id = resp.get_json()["id"]

    resp = client.get(f"/users/{user_id}")
    assert resp.status_code == 200
    assert resp.get_json()["name"] == "bob"
