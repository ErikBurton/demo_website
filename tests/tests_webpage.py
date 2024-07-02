import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSimpleWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("i/Users/erikb/Desktop/demo/index.html")  # Replace with the correct path to your index.html file

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
