import pytest

# @pytest.fixture()  => This is only for setup like/type case
@pytest.yield_fixture()  # or if we want to do at module level then use scope="module"
def xyz():
    print("SetUp - Once before every method")
    yield
    print("Teardown- Once after every method")


def testmethod1(xyz):
    print("Test method1")


def testmethod2(xyz):
    print("Test method2")
