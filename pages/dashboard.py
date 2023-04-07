from pages.base_page import BasePage

class Dashboard(BasePage):
    language_button_xpath = "//ul//div[@role='button' and ./div/span[text()='English']]"
    players_button_xpath = "//ul//div[@role='button' and ./div/span[text()='Players']]"
    main_page_button = "//ul//div[@role='button' and ./div/span[text()='Main page']]"
    sign_out_button = "//ul//div[@role='button' and ./div/span[text()='Sign out']]"
    add_player_button = "//div//a//span[text()='Dev team contact']"
    dev_team_contact_button = "//div//a//span[text()='Dev team contact']"
