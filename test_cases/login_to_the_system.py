import time
import unittest
import os
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()
    def test_log_into_the_system(self):
        login_page = LoginPage(self.driver)
        login_page.title_of_page() # zachodzi 1wsza asercja
        login_page.assert_login_panel_title()
        login_page.type_in_email("user01@getnada.com")
        login_page.type_in_password("Test-1234")
        login_page.click_sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_sign_out()
        login_page.title_of_page()



