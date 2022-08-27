import pytest

# @pytest.fixture()  => This is only for setup like/type case
@pytest.yield_fixture()  # or if we want to do at module level then use scope="module"
def xyzz():
    print("SetUp - Once before every method")
    yield
    print("Teardown- Once after every method")


def testmethodabc(xyzz):
    print("Test methodabc")


def testmethoddef(xyzz):
    print("Test methoddef")
