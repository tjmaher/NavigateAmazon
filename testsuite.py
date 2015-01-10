import unittest

from test_Login import TestLogin

class TestSuite(unittest.TestSuite):


	def suite():
		suite = unittest.TestSuite() # Creating a TestSuite object
		suite.addTest(TestLogin('test_waitForPageLoad'))
		return suite

if __name__ == "__main__":
	unittest.main()




