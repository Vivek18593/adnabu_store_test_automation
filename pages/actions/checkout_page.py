from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators import Locators

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self, wait):
        product_name = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.CHECKOUT_PRODUCT_NAME)))
        actual_product_name = product_name.text.strip().lower()
        return actual_product_name
        

    


