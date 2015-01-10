from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

class TestSearch(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		# driver = Ie()
		# driver = webdriver.Chrome()
		driver.get("http://www.amazon.com")


	def test_SearchForKeyword(self):
		element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'twotabsearchtextbox')))
		searchbox = driver.find_element_by_id("twotabsearchtextbox")
		searchbox.clear()
		searchbox.send_keys('selenium', Keys.RETURN)

	def tearDown(self):
		driver.quit()

if __name__ == "__main__":
	unittest.main() 