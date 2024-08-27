import pytest



from tests.conftest import client

user_token = None

@pytest.mark.asyncio
async def test_register_user(client):
    url = client.app.url_path_for('user_register')
    register_user_data = dict(
        name='test',
        hashed_password="test",
        email='emial@mail.ru'
    )
    response = client.post(
        url,
        json=register_user_data
    )

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_login_user(client):
    url = client.app.url_path_for('user_login')
    login_user_data = dict(
        password="test",
        email='emial@mail.ru'
    )
    response = client.post(
        url,
        json=login_user_data
    )
    user_token = response.json()['token']
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_authenticate_and_get_data(client):
    url = client.app.url_path_for('user_login')
    login_user_data = dict(
        password="test",
        email='emial@mail.ru'
    )
    response = client.post(
        url,
        json=login_user_data
    )
    token = response.json()['token']
    assert response.status_code == 200


    url = client.app.url_path_for('user_list')
    headers = {
        'Authorization': f"Bearer {token}"
    }
    response = client.get(
        url,
        headers=headers
    )
    assert response.json()[0]['name'] == 1