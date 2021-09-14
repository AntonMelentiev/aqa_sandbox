import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_API_URL, BASE_URL


def test_open_games_page__admin_user__page_available(driver, header_logged_out, header_logged_in_admin, home_page):
    username = "admin"
    password = "Admin123!"
    requests.post(
        url=f"{BASE_API_URL}/sign_up",
        json={"email": "admin@test.test", "username": username, "password": password}
    )
    requests.post(
        url=f"{BASE_API_URL}/debug/update_user_to_admin",
        json={"username": username},
    )

    home_page.open()
    header_logged_out._init_elements()
    header_logged_out.login(username=username, password=password)
    header_logged_in_admin._init_elements()
    header_logged_in_admin.open_game_list()

    WebDriverWait(driver=driver, timeout=2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/button'))
    )
    assert driver.current_url == f"{BASE_URL}admin/games"
