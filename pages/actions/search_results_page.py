from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators import Locators
import pytest

class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product_from_search_result_page(self, product_name, wait):
        search_result_items = wait.until(EC.visibility_of_all_elements_located((By.XPATH, Locators.SEARCH_RESULT_ITEMS)))
        for item in search_result_items:
            if item.text.strip().lower() == product_name.lower():
                item.click()
                break
        else:
            pytest.fail(f"Product '{product_name}' not found in the search results!")

