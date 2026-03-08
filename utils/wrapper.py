from utils.read_config import ReadConfig
from utils.testdata_reader import DataReader
from pages.actions.home_page import HomePage
from pages.actions.login_page import LoginPage
from pages.actions.product_page import ProductPage
from pages.actions.search_results_page import SearchResultPage
from pages.actions.checkout_page import CheckoutPage

class ObjectWrapper:
    def __init__(self, driver):
        self.config = ReadConfig()
        self.data_reader = DataReader()
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.product_page = ProductPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.checkout_page = CheckoutPage(driver)





