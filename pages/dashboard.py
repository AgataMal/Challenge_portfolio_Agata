import time

from pages.base_page import BasePage

class Dashboard(BasePage):
    
    left_menu_buttons_pattern = "//ul//div[@role='button' and ./div/span[text()='{}']]"

    language_button_en_xpath = left_menu_buttons_pattern.format("English")
        
    players_button_en_xpath = left_menu_buttons_pattern.format("Players")    
    
    main_page_en_button_xpath = left_menu_buttons_pattern.format("Main page")    
    
    sign_out_en_button_xpath = left_menu_buttons_pattern.format("Sign out")

    add_player_button = "//div//a//span[text()='Add player']"

    dev_team_contact_button = "//div//a//span[text()='Dev team contact']"

    login_url = 'https://scouts-test.futbolkolektyw.pl/en'

    expected_title = "Scouts panel"


    """
        User activity list links
    """
    users_activity_pattern = "//div[./h6/following-sibling::a]/a[{}]"
    users_activity_list_1 = users_activity_pattern.format("1")
    users_activity_list_2 = users_activity_pattern.format("2")
    users_activity_list_3 = users_activity_pattern.format("3")
    users_activity_list_4 = users_activity_pattern.format("4")
    users_activity_list_5 = users_activity_pattern.format("5")

    def title_of_page(self):
        self.wait_for_the_element_to_be_clickable(self.add_player_button)
        assert self.get_page_title(self.login_url) == self.expected_title

    def go_to_add_a_player(self):
        self.click_on_the_element(self.add_player_button)

    def click_sign_out(self):
        self.wait_for_the_element_to_be_clickable(self.sign_out_en_button_xpath)
        self.click_on_the_element(self.sign_out_en_button_xpath)

