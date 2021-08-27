from selenium.webdriver.remote.webdriver import WebDriver

from pages.components.header import Header


class BasePage:
    def __init__(self, driver: WebDriver, header: Header):
        self._driver = driver
        self.header = header

    @property
    def _url(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError
