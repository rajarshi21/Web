import unittest

class AppTesting(unittest.TestCase):
    @unittest.skip("skipping just like that")
    def test_search(self):
        print("Test search")

    @unittest.skipIf("raj" == "raj", "some msg")
    def test_advsearch(self):
        print("Adv search")

    def test_prepaidRecharge(self):
        print("Pre paid recharge")

    def test_postpaidRecharge(self):
        print("Post paid recharge")


if __name__ == "__main__":
    unittest.main()
