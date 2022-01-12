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

    ##############################
    # Login dropdown
    ##############################
    @property
    def _login_dropdown(self):
        return self._driver.find_element_by_id("login_dropdown")

    @property
    def _username_input(self):
        return self._driver.find_element_by_id("username_input")

    @property
    def _password_input(self):
        return self._driver.find_element_by_id("password_input")

    @property
    def _submit_login_btn(self):
        return self._driver.find_element_by_id("login_btn")

    ##############################
    # User dropdown
    ##############################
    @property
    def _user_dropdown(self):
        return self._driver.find_element_by_id("user_dropdown")

    @property
    def _user_page_lnk(self):
        return self._driver.find_element_by_id("UNuser")

    ##############################
    # Main navigation
    ##############################
    @property
    def _admin_page_nav_btn(self):
        return self._driver.find_element_by_id("HBadmingames")

    ####################################################################################################################
    # Methods
    ####################################################################################################################

    @allure.step
    def open_login_dropdown(self):
        self._login_dropdown.click()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "login_btn"))
        )

    @allure.step
    def login(self, username: str, password: str, timeout: Union[float, int] = TIMEOUT):
        self.open_login_dropdown()
        self._username_input.send_keys(username)
        self._password_input.send_keys(password)
        self._submit_login_btn.click()

        WebDriverWait(driver=self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "user_dropdown")),
            message="User login timeout. User dropdown not shown.",
        )

    @allure.step
    def open_user_dropdown(self):
        self._user_dropdown.click()
        WebDriverWait(driver=self._driver, timeout=2).until(
            expected_conditions.visibility_of_element_located((By.ID, "UNuser"))
        )

    @allure.step
    def open_user_page_from_dropdown(self):
        self.open_user_dropdown.click()
        self._user_page_lnk.click()

    @allure.step
    def open_game_list(self):
        self._admin_page_nav_btn.click()
