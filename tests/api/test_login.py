from http import HTTPStatus

import pytest
import requests

from config import BASE_API_URL


def test_login__correct_user__user_logged_in(test_user):
    response = requests.post(
        url=f"{BASE_API_URL}/login_web",
        json={"username": test_user["username"], "password": test_user["password"]},
    )

    resp_data = response.json()
    token_web = resp_data.pop("token_web", None)
    assert token_web is not None, "No token_web in response"
    assert resp_data == {"username": test_user["username"], "roles": []}


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
        url=f"{BASE_API_URL}/login_web",
        json={"username": login, "password": pwd},
    )

    resp_data = response.json()
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert resp_data == {"error": "Wrong username or password!"}
