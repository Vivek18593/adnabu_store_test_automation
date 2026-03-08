from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.locators import Locators

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def select_product(self, wait):
        add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.ADD_TO_CART)))
        add_to_cart_button.click()
        checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, Locators.CHECKOUT)))
        checkout_button.click()
        

    



