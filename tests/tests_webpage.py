from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class TestSimpleWebsite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_driver_path = '/chromedriver'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Add your test methods here

if __name__ == "__main__":
    unittest.main()
