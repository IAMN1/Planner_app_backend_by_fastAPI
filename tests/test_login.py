import httpx
import pytest

from models.users import User
from auth.hash_password import HashPassword


@pytest.mark.asyncio
async def test_sign_new_user(default_client: httpx.AsyncClient) -> None:
    payload = {
        "email": "testuser@mail.com",
        "password": "testPassword"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    test_response = {
        "message": "User successfully registered!"
    }

    response = await default_client.post("/user/signup", json=payload)

    assert response.status_code == 200
    assert response.json() == test_response

@pytest.fixture(scope="function")
async def mock_user() -> User:

    hasher = HashPassword()
    hash_pswd = hasher.create_hash("testPassword")
    
    new_user = User(
        email="testuser123@mail.com",
        password=hash_pswd
    )

    await User.insert(new_user)
    
    yield new_user

@pytest.mark.asyncio
async def test_sign_user_in(default_client: httpx.AsyncClient, mock_user: User) -> None:
    payload = {
        "username": mock_user.email,
        "password": "testPassword"
    }

    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = await default_client.post(
        '/user/signin',
        data=payload, 
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["token_type"] == "Bearer"