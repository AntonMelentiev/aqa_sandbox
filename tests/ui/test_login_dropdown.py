import pytest
from selenium.common.exceptions import TimeoutException

from config import BASE_URL


def test_login_from_home__correct_user__user_logged_in(driver, home_page, test_user):
    home_page.open()
    home_page.header.login(username=test_user["username"], password=test_user["password"])

    user_dropdown = driver.find_element_by_id("user_dropdown")
    assert user_dropdown.text == test_user["username"]
    assert driver.current_url == BASE_URL


@pytest.mark.parametrize(
    argnames=("test_username", "test_password"),
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
def test_login_from_home__incorrect_user__user_failed_to_login(home_page, test_username, test_password):
    home_page.open()

    with pytest.raises(TimeoutException):
        home_page.header.login(username=test_username, password=test_password, timeout=0.5)
