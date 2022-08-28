class TestPy:

    def __init__(self):
        print('Inside init')

    def add(self, x, y):
        return x + y

    def substract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = TestPy()
    print(test.add(1, 2))

