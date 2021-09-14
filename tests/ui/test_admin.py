from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import BASE_URL


def test_open_games_page__admin_user__page_available(
    driver, header_logged_out, header_logged_in_admin, home_page, test_admin
):
    home_page.open()
    header_logged_out._init_elements()
    header_logged_out.login(username=test_admin["username"], password=test_admin["password"])
    header_logged_in_admin._init_elements()
    header_logged_in_admin.open_game_list()

    WebDriverWait(driver=driver, timeout=2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/button'))
    )
    assert driver.current_url == f"{BASE_URL}admin/games"
