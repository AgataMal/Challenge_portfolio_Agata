import unittest
from test_cases.add_a_player import TestLoginPage as add_player
from test_cases.login_page import TestLoginPage as login_page
from test_cases.login_to_the_system import TestLoginPage as login_to_system
from unittest.loader import makeSuite


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(add_player))
   test_suite.addTest(makeSuite(login_page))
   test_suite.addTest(makeSuite(login_to_system))




   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())