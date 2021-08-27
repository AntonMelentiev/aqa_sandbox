import pytest

from selenium.common.exceptions import TimeoutException

from config import BASE_URL


def test_login_from_home__correct_user__user_logged_in(driver, header, home_page):
    username = "test"
    password = "Test123!"

    home_page.open()
    header.login(username=username, password=password)

    assert header._user_dropdown.text == username
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
def test_login_from_home__incorrect_user__user_failed_to_login(header, home_page, login, pwd):
    home_page.open()

    with pytest.raises(TimeoutException):
        header.login(username=login, password=pwd, timeout=0.5)
