from typing import Union

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT


class Header:
    def __init__(self, driver: webdriver):
        self._driver = driver

    @allure.step
    def open_login_dropdown(self):
        login_dropdown = self._driver.find_element_by_id("login_dropdown")
        login_dropdown.click()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "login_btn"))
        )

    @allure.step
    def login(self, username: str, password: str, timeout: Union[float, int] = TIMEOUT):
        self.open_login_dropdown()
        username_input = self._driver.find_element_by_id("username_input")
        password_input = self._driver.find_element_by_id("password_input")
        submit_login_btn = self._driver.find_element_by_id("login_btn")
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_login_btn.click()

        WebDriverWait(driver=self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "user_dropdown")),
            message="User login timeout. User dropdown not shown.",
        )

    @allure.step
    def open_user_dropdown(self):
        user_dropdown = self._driver.find_element_by_id("user_dropdown")
        user_dropdown.click()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "UNuser"))
        )

    @allure.step
    def open_user_page_from_dropdown(self):
        self.open_user_dropdown.click()
        user_page_lnk = self._driver.find_element_by_id("UNuser")
        user_page_lnk.click()

    @allure.step
    def open_game_list(self):
        admin_page = self._driver.find_element_by_id("HBadmingames")
        admin_page.click()
