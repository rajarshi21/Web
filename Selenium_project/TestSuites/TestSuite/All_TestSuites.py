import unittest
import time
from TestSuites.Package1.TC_logintest import LoginTest
from TestSuites.Package1.TC_signuptest import SignupTest

from TestSuites.Package2.TC_paymentreturnstest import PaymentReturnsTest
from TestSuites.Package2.TC_paymenttest import PaymentTestInTest

# Get all the tests from all the files.
# Sanity test for e.g
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
# Functional test for e.g
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTestInTest)


# Creating sanity test suites.
sanity = unittest.TestSuite([tc1, tc2])

# Creating functional test suites.
functional = unittest.TestSuite([tc3, tc4])

# Creating master test suites.
master = unittest.TestSuite([tc1, tc2, tc3, tc4])

# run suite
# unittest.TextTestRunner().run(sanity)
# unittest.TextTestRunner().run(functional)
unittest.TextTestRunner().run(master)










