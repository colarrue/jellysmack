def test_episode(client):

    response = client.get(f"/episodes/{2}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Lawnmower Dog"
    assert data["episode"] == "S01E02"
    assert data["characters"][1]["name"] == "Morty Smith"
