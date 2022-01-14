def test_comment(client):
    # Add comment to episode
    response = client.post("/comments", json={"content": "test comment", "episode_id": 2})
    assert response.status_code == 201
    response = client.get(f"/comments/{1}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["content"] == "test comment"
    assert data["episode_id"] == 2
    # Get episode and check comment
    response = client.get(f"/episodes/{2}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["comments"][0]["content"] == "test comment"
