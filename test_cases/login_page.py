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

    def test_no_password_provided(self):
        login_page = LoginPage(self.driver)
        login_page.title_of_page()  # zachodzi 1wsza asercja
        login_page.assert_login_panel_title()
        login_page.type_in_email("user06@getnada.com")
        login_page.click_sign_in()
        login_page.assert_missing_password()

    def test_invalid_password_provided(self):
        login_page = LoginPage(self.driver)
        login_page.title_of_page()  # zachodzi 1wsza asercja
        login_page.assert_login_panel_title()
        login_page.type_in_email("user06@getnada.com")
        login_page.type_in_password("invalid")
        login_page.click_sign_in()
        login_page.assert_invalid_password()

    def test_select_language(self):
        login_page = LoginPage(self.driver)
        login_page.title_of_page()
        login_page.click_on_select_language()
        time.sleep(1)
        login_page.click_on_polish_language()
        time.sleep(2)
        login_page.assert_translated()
    @classmethod
    def tearDown(self):
        self.driver.quit()