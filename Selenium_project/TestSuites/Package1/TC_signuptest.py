import unittest


class SignupTest(unittest.TestCase):
    def test_Signupbyemail(self):
        print("sign up by email test")
        self.assertTrue(True)

    def test_signupbyfacebook(self):
        print("sign up by facebook test")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("sign up by twitter test")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
