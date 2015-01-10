# NavigateAmazon
Navigating Amazon.com with Selenium, Python 2.7 and unittest

Start date: 1/9/2015:

NavigateAmazon uses Unittest (PyUnit) -- a Python version of JUnit -- to manage running all testing scenarios.   

Each individual test case (such as test_Search.py and test_Login.py) contains setup and shutdown modules for each test using the setUp() and tearDown() methods, along with individual tests that are executed.  

Testsuite.py is compilation of all tests for the NavigateAmazon project, aggregating all test cases. By running this test suite, all other tests that have been imported to it are executed. 

Test Cases, and the scenarios they test: 
* test_Login.py: Tests Amazon.com's login functionality when a member logs into the system. 
* test_Search.py: Tests Amazon.com's search functionality. 
