from http import HTTPStatus

import allure
import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config import BASE_API_URL
from pages.home_page import HomePage
from utils import get_screenshot_name


# See http://doc.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()

    yield driver

    try:
        if request.node.rep_call.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=get_screenshot_name(request),
                attachment_type=allure.attachment_type.PNG,
            )
    finally:
        driver.quit()


@pytest.fixture
def home_page(driver) -> HomePage:
    yield HomePage(driver=driver)


@pytest.fixture
def test_user():
    username = "test"
    password = "Test123!"
    resp = requests.post(
        url=f"{BASE_API_URL}/sign_up", json={"email": "test@test.test", "username": username, "password": password}
    )

    if resp.status_code != HTTPStatus.OK:
        assert False, "Cant create test user"

    yield {"username": username, "password": password}

    requests.post(url=f"{BASE_API_URL}/debug/remove_user", json={"username": username})


@pytest.fixture
def test_admin():
    username = "admin"
    password = "Admin123!"
    resp1 = requests.post(
        url=f"{BASE_API_URL}/sign_up", json={"email": "admin@test.test", "username": username, "password": password}
    )

    resp2 = requests.post(
        url=f"{BASE_API_URL}/debug/update_user_to_admin",
        json={"username": username},
    )

    if resp1.status_code != HTTPStatus.OK or resp2.status_code != HTTPStatus.OK:
        assert False, "Cant create test admin user"

    yield {"username": username, "password": password}

    requests.post(url=f"{BASE_API_URL}/debug/remove_user", json={"username": username})
