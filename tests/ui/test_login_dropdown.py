import pytest
import requests
from selenium.common.exceptions import TimeoutException

from config import BASE_API_URL, BASE_URL


def test_login_from_home__correct_user__user_logged_in(driver, header_logged_out, header_logged_in, home_page):
    username = "test"
    password = "Test123!"
    requests.post(
        url=f"{BASE_API_URL}/sign_up",
        json={"email": "test@test.test", "username": username, "password": password}
    )

    home_page.open()
    header_logged_out.login(username=username, password=password)

    header_logged_in._init_elements()
    assert header_logged_in._user_dropdown.text == username
    assert driver.current_url == BASE_URL


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
def test_login_from_home__incorrect_user__user_failed_to_login(header_logged_out, home_page, login, pwd):
    home_page.open()

    with pytest.raises(TimeoutException):
        header_logged_out.login(username=login, password=pwd, timeout=0.5)


