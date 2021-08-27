from typing import List, Union

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import TIMEOUT


class Header:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._lazy_init_complete = False

        self._is_logged_in = False
        self._is_admin = False

    def _lazy_init(self):
        if not self._lazy_init_complete:
            if self._is_logged_in:
                self._user_dropdown = self._driver.find_element_by_id("user_dropdown")
            else:
                self._login_dropdown = self._driver.find_element_by_id("login_dropdown")

            self._lazy_init_complete = True

    def _lazy_init_dropdown(self):
        if self._is_logged_in:
            self._user_page_lnk = self._driver.find_element_by_id("UNuser")
        else:
            self._username_input = self._driver.find_element_by_id("username_input")
            self._password_input = self._driver.find_element_by_id("password_input")
            self._submit_login_btn = self._driver.find_element_by_id("login_btn")

    def _remove_attrs_if_exists(self, attr_list: List[str]):
        for attr_name in attr_list:
            if hasattr(self, attr_name):
                delattr(self, attr_name)

    @allure.step("set_state")
    def _set_state(self, logged_in: bool = None, is_admin: bool = None):
        if logged_in is None:
            logged_in = self._is_logged_in
        if is_admin is None:
            is_admin = self._is_admin

        if logged_in:
            self._remove_attrs_if_exists(
                attr_list=["_login_dropdown", "_username_input", "_password_input", "_submit_login_btn"]
            )
            self._user_dropdown = self._driver.find_element_by_id("user_dropdown")

            if is_admin:
                pass  # TODO: add admin page element

        else:
            self._remove_attrs_if_exists(attr_list=["_user_dropdown", "_user_page_lnk"])
            self._login_dropdown = self._driver.find_element_by_id("login_dropdown")

        self._is_logged_in = logged_in

    @allure.step
    def open_login_dropdown(self):
        self._login_dropdown.click()
        self._lazy_init_dropdown()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "login_btn"))
        )

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
        self._set_state(logged_in=True, is_admin=is_admin)

    @allure.step
    def open_user_dropdown(self):
        self._user_dropdown.click()
        self._lazy_init_dropdown()
        WebDriverWait(driver=self._driver, timeout=10).until(
            expected_conditions.visibility_of_element_located((By.ID, "UNuser"))
        )

    @allure.step
    def open_user_page_from_dropdown(self):
        self.open_user_dropdown.click()
        self._user_page_lnk.click()
