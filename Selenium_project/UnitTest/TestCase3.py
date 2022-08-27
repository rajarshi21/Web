import unittest


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("teardown Module")


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setUp method")

    @classmethod
    def tearDown(cls):
        print("tear down method")

    @classmethod
    def setUpClass(cls):
        print("set up class")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def test_search(self):
        print("Test search")

    def test_advsearch(self):
        print("Adv search")

    def test_prepaidRecharge(self):
        print("Pre paid recharge")

    def test_postpaidRecharge(self):
        print("Post paid recharge")


if __name__=="__main__":
    unittest.main()