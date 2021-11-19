from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_URL


def test_open_games_page__admin_user__page_available(driver, home_page, test_admin):
    home_page.open()
    home_page.header.login(username=test_admin["username"], password=test_admin["password"])
    home_page.header.open_game_list()

    WebDriverWait(driver=driver, timeout=2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/button'))
    )
    assert driver.current_url == f"{BASE_URL}admin/games"
