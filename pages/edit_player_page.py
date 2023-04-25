from pages.base_page import BasePage


class EditPlayerPage(BasePage):
    def title_of_page(self, expected_name, expected_surname):

        assert self.get_page_title(None) == f"Edit player {expected_name} {expected_surname}"
