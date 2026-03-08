from selenium.webdriver.common.by import By
from pages.locators.locators import Locators
import pytest

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, search_value):
        search_icon = self.driver.find_element(By.XPATH, Locators.SEARCH_ICON)
        search_icon.click()
        search_input_field = self.driver.find_element(By.XPATH, Locators.SEARCH_FIELD)
        search_input_field.send_keys(search_value)

    def select_search_suggestion(self, search_value):
        suggestions = self.driver.find_elements(By.XPATH, Locators.SEARCH_SUGGESTION_LIST)
        for option in suggestions:
            text = option.text.strip().lower()
            if search_value.lower() in text or text in search_value.lower():
                option.click()
                return
        pytest.fail(f"{search_value} not found in suggestions")





