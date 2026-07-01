from __future__ import annotations


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_list_tickets(client):
    r = client.get("/tickets?limit=10")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert {"id", "title", "description", "status", "created_at", "updated_at"}.issubset(
        data[0].keys()
    )


def test_filter_by_status(client):
    r = client.get("/tickets?status=open")
    assert r.status_code == 200
    assert all(t["status"] == "open" for t in r.json())


def test_get_ticket(client):
    r = client.get("/tickets")
    tid = r.json()[0]["id"]
    r2 = client.get(f"/tickets/{tid}")
    assert r2.status_code == 200
    assert r2.json()["id"] == tid


def test_patch_status(client):
    r = client.get("/tickets")
    tid = r.json()[0]["id"]
    r2 = client.patch(f"/tickets/{tid}/status", json={"status": "resolved"})
    assert r2.status_code == 200
    assert r2.json()["status"] == "resolved"
