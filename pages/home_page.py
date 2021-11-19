import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT
from config import BASE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    _url = BASE_URL

    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

    @allure.step("open_home_page")
    def open(self):
        self._driver.get(self._url)
        WebDriverWait(driver=self._driver, timeout=TIMEOUT).until(
            expected_conditions.presence_of_element_located((By.ID, "game_list"))
        )
