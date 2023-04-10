from pages.base_page import BasePage

class Dashboard(BasePage):
    text_input_pattern = "//form//input[@type=\"text\" and @name=\"{}\"]"
    my_team_input = text_input_pattern.format("myTeam")
    my_enemy_input = text_input_pattern.format("myEnemy")
    my_enemyTeamScore_input = text_input_pattern.format("enemyTeamScore")
    my_myTeamScore_input = text_input_pattern.format("myTeamScore")
    date_input = "//form//input[@type=\"date\" and @name=\"date\"]"
    match_at_home_input = "//form//input[@type=\"radio\" and @name=\"matchAtHome\"]"

    left_menu_buttons_pattern = "//ul//div[@role='button' and ./div/span[text()='{}']]"
    matches_button = left_menu_buttons_pattern.format("Matches")
    reports_button = left_menu_buttons_pattern.format("Reports")
    players_button = left_menu_buttons_pattern.format("Players")
    sign_out_button = left_menu_buttons_pattern.format("Sign out")



