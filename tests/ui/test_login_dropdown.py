import pytest
from selenium.common.exceptions import TimeoutException

from config import BASE_URL


def test_login_from_home__correct_user__user_logged_in(
    driver, header_logged_out, header_logged_in, home_page, test_user
):
    home_page.open()
    header_logged_out.login(username=test_user["username"], password=test_user["password"])

    header_logged_in._init_elements()
    assert header_logged_in._user_dropdown.text == test_user["username"]
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
