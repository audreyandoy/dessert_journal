def test_get_all_desserts_db_return_empty_list(client):
    response = client.get('/desserts')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_dessert(client, two_desserts):
    response = client.get("desserts/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Taro Bubble Tea",
        "description": "Taro flavored bubble tea with tapioca pearls"
    }