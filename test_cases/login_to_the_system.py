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
        user_login = LoginPage(self.driver)
        user_login.title_of_page() # zachodzi 1wsza asercja
        user_login.type_in_email("user01@getnada.com")
        time.sleep(1)
        user_login.type_in_password("Test-1234")
        time.sleep(2)
        user_login.click_sign_in()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()



