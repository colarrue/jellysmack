def test_characters(client):
    response = client.get(f"/characters/{3}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Summer Smith"
    assert data["status"] == "Alive"
    assert data["species"] == "Human"
