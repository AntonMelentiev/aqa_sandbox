from selenium.webdriver.remote.webdriver import WebDriver

from page_elements.header import Header


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self.header = Header(driver=self._driver)

    @property
    def _url(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError
