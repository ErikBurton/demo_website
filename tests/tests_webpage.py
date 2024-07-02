import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSimpleWebsite(unittest.TestCase):

   from selenium import webdriver

class TestSimpleWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = '/usr/local/bin/chromedriver'
        cls.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_change_text_button(self):
        driver = self.driver
        button = driver.find_element(By.ID, "change-text-btn")
        button.click()
        message = driver.find_element(By.ID, "welcome-message").text
        self.assertEqual(message, "Text Changed!")

if __name__ == "__main__":
    unittest.main()
