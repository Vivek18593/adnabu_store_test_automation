from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def driver():
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




