import time

from pages.base_page import BasePage


class AddPlayer(BasePage):

    login_url = 'https://scouts-test.futbolkolektyw.pl/en'

    expected_title = "Add player"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.login_url) == self.expected_title



