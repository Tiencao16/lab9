import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearch:
    def setup_method(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def teardown_method(self):
        self.driver.quit()

    def test_search_products(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(items) > 0
        print(f"✅ Test Search: Tìm thấy {len(items)} sản phẩm - PASSED")
