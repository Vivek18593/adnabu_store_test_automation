from selenium.webdriver.support.ui import WebDriverWait
from utils.wrapper import ObjectWrapper
import pytest

class TestProductSearchAndCheckout:

    def test_product_search(self, driver):
        # Common wait
        wait = WebDriverWait(driver, 10)

        # Wrapper class object
        wrapper = ObjectWrapper(driver)

        # Getting testdata
        base_url = wrapper.config.get_application_url()
        password = wrapper.config.get_password()
        search_value = wrapper.data_reader.get_search_value()
        product_name = wrapper.data_reader.get_product_name()

        # Test case execution
        wrapper.login_page.authenticate_store(base_url, password)
        wrapper.home_page.search_product(search_value)
        wrapper.home_page.select_search_suggestion(search_value)
        wrapper.search_result_page.select_product_from_search_result_page(product_name, wait)
        wrapper.product_page.select_product(wait)

        # Assertion
        actual_product_name = wrapper.checkout_page.get_product_name(wait)
        assert actual_product_name == product_name.strip().lower(), f"Searched product '{product_name}', but got '{actual_product_name}'"

        



