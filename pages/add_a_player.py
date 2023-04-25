import time

from pages.base_page import BasePage


class AddPlayer(BasePage):

    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    name_field_xpath = "//input[@name=\"name\" and @type=\"text\"]"
    surname_field_xpath = "//input[@name=\"surname\" and @type=\"text\"]"
    date_field_xpath ="//input[@name=\"age\" and @type=\"date\"]"
    position_field_xpath = "//input[@name=\"mainPosition\" and @type=\"text\"]"
    submit_button_xpath = "//form//button[@type=\"submit\" and ./span[contains(text(), SUBMIT)]]"
    expected_title = "Add player"

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.login_url) == self.expected_title

    def add_name(self, name):
        self.wait_for_the_element_to_be_clickable(self.name_field_xpath)
        self.field_send_keys(self.name_field_xpath, name)

    def add_surname(self, surname):
        self.wait_for_the_element_to_be_clickable(self.surname_field_xpath)
        self.field_send_keys(self.surname_field_xpath, surname)
    def add_date(self, date):
        self.wait_for_the_element_to_be_clickable(self.date_field_xpath)
        self.field_send_keys(self.date_field_xpath, date)

    def add_main_position(self, position):
        self.wait_for_the_element_to_be_clickable(self.position_field_xpath)
        self.field_send_keys(self.position_field_xpath, position)

    def click_submit(self):
        self.wait_for_the_element_to_be_clickable(self.submit_button_xpath)
        self.click_on_the_element(self.submit_button_xpath)




