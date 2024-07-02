from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import os

class TestSimpleWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = '/usr/local/bin/chromedriver'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_change_text(self):
        # Update the path to the HTML file
        file_path = os.path.abspath("/Users/erikb/Desktop/demo/index.html")
        self.driver.get(f"file://{file_path}")
        button = self.driver.find_element("id", "change-text-btn")
        button.click()
        message = self.driver.find_element("id", "welcome-message")
        self.assertEqual(message.text, "Text Changed!")

if __name__ == "__main__":
    unittest.main()
