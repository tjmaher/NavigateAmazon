from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import unittest

class TestLogin(unittest.TestCase):

	global username # Not the best solution, declaring a global variable 
	global password #     here but okay for demonstration purposes. 
	
	username = 'amzn.tester23@gmail.com'
	password = 'amzntester23'
	
	
	def setUp(self):
		"""Setup method opens Amazon.com in the chosen browser and initializes mouse controls"""
		global driver # Global variable to hold the browser being used
		global mouse  # Global variable to hold the mouse controls. 
		driver = webdriver.Firefox() # Use Firefox browser to test... Default browser
		# driver = Ie() # Needs C:\Python27\IEDriverServer.exe to run IE
		# driver = webdriver.Chrome() # Needs C:\Python27\chromedriver.exe to run Chrome
		driver.get("http://www.amazon.com")
		mouse = webdriver.ActionChains(driver) # Activates the mouse controls
		
	def test_ValidUsernameSignIn(self):
		"""Go to SignIn page, enter designated username and password, and select Sign In button"""
		# The SignIn button that must be clicked is: class="nav-action-button"		
		button_SignIn = driver.find_element_by_class_name('nav-action-button')

		# Hover on span element by mouse and click on it:
		mouse.move_to_element(button_SignIn).click().perform()		

		# Wait until the Sign In page is fully loaded before continuing. 
		element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'ap_email')))

		# Enter the username into the username textbox
		txtboxUserName = driver.find_element_by_id('ap_email')
		txtboxUserName.clear()
		txtboxUserName.send_keys(username)

		# Enter the password into the password textbox
		txtboxUserName = driver.find_element_by_id('ap_password')
		txtboxUserName.clear()
		txtboxUserName.send_keys(password)		
		
		# Select the Sign In button
		buttonSignIn = driver.find_element_by_id('signInSubmit-input')
		buttonSignIn.click()
		
		
		
	def tearDown(self):
		"""Shutdown method that closes the browser."""
		driver.quit()

if __name__ == "__main__":
	unittest.main() 
