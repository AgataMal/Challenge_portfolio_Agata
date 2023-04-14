from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    login_panel_title = "//h5"
    password_field_xpath ="//input[@id=\"password\" and @type=\"password\"]"
    sign_in_button_xpath = "//form//button[@type=\"submit\" and ./span[contains(text(), SIGN-IN)]]"
    remind_password_xpath = "//form//div//child::a"
    language_select_dropdown_xpath = "//form//child::div[@role=\"button\"]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = "Scouts panel - sign in"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def assert_login_panel_title(self):
        self.assert_element_text(self.driver, self.login_panel_title, "Scouts Panel")



