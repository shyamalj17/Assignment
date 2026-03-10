from jsonschema import validate
from schemas.post_schema import post_schema


def test_get_posts_status_code(api_client):

    response = api_client.get_posts()

    assert response.status_code == 200


def test_get_posts_not_empty(api_client):

    response = api_client.get_posts()

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_validate_post_schema(api_client):

    response = api_client.get_post(1)

    data = response.json()

    validate(instance=data, schema=post_schema)


def test_validate_post_id(api_client):

    response = api_client.get_post(1)

    data = response.json()

    assert data["id"] == 1


# Negative test
def test_invalid_post_id(api_client):

    response = api_client.get_post(9999)

    assert response.status_code == 404 or response.json() == {}