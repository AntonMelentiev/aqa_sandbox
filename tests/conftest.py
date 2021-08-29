import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.components.header import Header
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
def header(driver):
    yield Header(driver=driver)


@pytest.fixture
def home_page(driver, header):
    yield HomePage(driver=driver, header=header)
