import pytest
import requests

from config import BASE_API_URL


def test_login__correct_user__user_logged_in():
    username = "test"
    password = "Test123!"
    expected_response_keys = ["team", "token", "username"]

    response = requests.post(
        url=f"{BASE_API_URL}/login",
        json={"username": username, "password": password},
    )
    resp_data = response.json()
    resp_keys = resp_data.keys()

    assert sorted(expected_response_keys) == sorted(resp_keys)
    assert resp_data["username"] == username
    assert resp_data["team"] is None


@pytest.mark.parametrize(
    argnames=("login", "pwd"),
    argvalues=(
        ("test", ""),
        ("test", "wrong_pass"),
        ("wrong_user", "some_pass"),
    ),
    ids=(
        "empty password",
        "wrong password",
        "wrong user",
    ),
)
def test_login__incorrect_user__user_failed_to_login(login, pwd):
    response = requests.post(
        url=f"{BASE_API_URL}/login",
        json={"username": login, "password": pwd},
    )

    resp_data = response.json()
    assert resp_data == {"error": "Wrong username or password!"}
