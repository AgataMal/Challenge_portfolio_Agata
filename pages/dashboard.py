from pages.base_page import BasePage

class Dashboard(BasePage):
    
    language_button_xpath = "//ul//div[@role='button' and ./div/span[text()='English']]"
    
    players_button_xpath = "//ul//div[@role='button' and ./div/span[text()='Players']]"
    
    main_page_button = "//ul//div[@role='button' and ./div/span[text()='Main page']]"
    
    sign_out_button = "//ul//div[@role='button' and ./div/span[text()='Sign out']]"
    
    add_player_button = "//div//a//span[text()='Dev team contact']"
    
    dev_team_contact_button = "//div//a//span[text()='Dev team contact']"

    """
        User activity list links
    """
    users_activity_pattern = "//div[./h6/following-sibling::a]/a[{}]"
    users_activity_list_1 = users_activity_pattern.format("1")
    users_activity_list_2 = users_activity_pattern.format("2")
    users_activity_list_3 = users_activity_pattern.format("3")
    users_activity_list_4 = users_activity_pattern.format("4")
    users_activity_list_5 = users_activity_pattern.format("5")



