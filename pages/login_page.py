from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath ="//input[@id=\"password\" and @type=\"password\"]"
    sign_in_button_xpath = "//form//button[@type=\"submit\" and ./span[contains(text(), SIGN-IN)]]"
    remind_password_xpath = "//form//div//child::a"
    language_select_dropdown_xpath = "//form//child::div[@role=\"button\"]"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
