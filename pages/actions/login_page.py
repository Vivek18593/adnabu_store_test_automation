from selenium.webdriver.common.by import By
from pages.locators.locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def authenticate_store(self, base_url, password):
        self.driver.get(base_url)
        self.driver.find_element(By.XPATH, Locators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.XPATH, Locators.ENTER_BUTTON).click()







