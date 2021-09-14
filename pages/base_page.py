from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def _url(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError
