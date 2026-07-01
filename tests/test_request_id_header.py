def test_sets_x_request_id_header(client) -> None:
    r = client.get("/health")
    assert "X-Request-ID" in r.headers
    assert r.headers["X-Request-ID"]


def test_echoes_incoming_x_request_id(client) -> None:
    rid = "test-request-id-123"
    r = client.get("/health", headers={"X-Request-ID": rid})
    assert r.headers.get("X-Request-ID") == rid
