from typing import Union

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT


class HeaderBase:
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._lazy_init_complete = False
        self._lazy_init_dropdown_complete = False


class HeaderLoggedOut(HeaderBase):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

    def _init_elements(self):
        if not self._lazy_init_complete:
            WebDriverWait(driver=self._driver, timeout=TIMEOUT).until(
                expected_conditions.presence_of_element_located((By.ID, "HBlogo"))
            )
            self._login_dropdown = self._driver.find_element_by_id("login_dropdown")
            self._lazy_init_complete = True

    def _lazy_init_dropdown(self):
        if not self._lazy_init_dropdown_complete:
            self._username_input = self._driver.find_element_by_id("username_input")
            self._password_input = self._driver.find_element_by_id("password_input")
            self._submit_login_btn = self._driver.find_element_by_id("login_btn")
            self._lazy_init_dropdown_complete = True

    @allure.step
    def open_login_dropdown(self):
        self._init_elements()
        self._login_dropdown.click()
        self._lazy_init_dropdown()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "login_btn"))
        )
        self._lazy_init_dropdown()

    @allure.step
    def login(self, username: str, password: str, is_admin: bool = False, timeout: Union[float, int] = None):
        if timeout is None:
            timeout = TIMEOUT

        self.open_login_dropdown()
        self._username_input.send_keys(username)
        self._password_input.send_keys(password)
        self._submit_login_btn.click()

        WebDriverWait(driver=self._driver, timeout=timeout).until(
            expected_conditions.visibility_of_element_located((By.ID, "user_dropdown")),
            message="User login timeout. User dropdown not shown.",
        )


class HeaderLoggedIn(HeaderBase):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

    def _init_elements(self):
        if not self._lazy_init_complete:
            WebDriverWait(driver=self._driver, timeout=TIMEOUT).until(
                expected_conditions.presence_of_element_located((By.ID, "HBlogo"))
            )
            self._user_dropdown = self._driver.find_element_by_id("user_dropdown")
            self._lazy_init_complete = True

    def _lazy_init_dropdown(self):
        if not self._lazy_init_dropdown_complete:
            self._user_page_lnk = self._driver.find_element_by_id("UNuser")
            self._lazy_init_dropdown_complete = True

    @allure.step
    def open_user_dropdown(self):
        self._init_elements()
        self._user_dropdown.click()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "UNuser"))
        )
        self._lazy_init_dropdown()

    @allure.step
    def open_user_page_from_dropdown(self):
        self.open_user_dropdown.click()
        self._user_page_lnk.click()


class HeaderLoggedInAdmin(HeaderLoggedIn):
    def __init__(self, driver: webdriver):
        super().__init__(driver=driver)

    def _init_elements(self):
        if not self._lazy_init_complete:
            WebDriverWait(driver=self._driver, timeout=TIMEOUT).until(
                expected_conditions.presence_of_element_located((By.ID, "HBlogo"))
            )
            self._user_dropdown = self._driver.find_element_by_id("user_dropdown")
            self._admin_page = self._driver.find_element_by_id("HBadmingames")
            self._lazy_init_complete = True

    @allure.step
    def open_game_list(self):
        self._init_elements()
        self._admin_page.click()
