def test_live(client):
    response = client.get("/health/live")
    expected = {"status": "ok"}
    assert response.status_code == 200
    assert response.get_json() == expected