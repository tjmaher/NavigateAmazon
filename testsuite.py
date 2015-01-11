import unittest

from test_Login import TestLogin
from test_Search import TestSearch

class TestSuite(unittest.TestSuite):

	def suite():
		suite = unittest.TestSuite() # Creating a TestSuite object
		suite.addTest(TestLogin('test_ValidUsernameSignIn'))
		suite.addTest(TestSearch('test_SearchForKeyword'))
		return suite

if __name__ == "__main__":
	unittest.main()




