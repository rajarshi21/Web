from numpy import random

# Random - intro
# Generate random number
# There are 2 types of random numbers - Truly random and Pseudo random number
x = random.randint(100)
print(x)
# Generate random array
print('Random int array')
x = random.randint(100, size=10)
print(x)
# Generate 2-D array with 3 rows and 5 cols
x = random.randint(100, size=(3, 5))
print('2-D array with random numbers with 3 rows and 5 cols')
print(x)
# Generate 1-D array containing 5 random floats
print('Print random floats 1-D array')
x = random.rand(5)
print(x)
print('Print random floats 2-D array')
x = random.rand(3, 5)
print(x)
# Generate random number from array
x = random.choice([3, 5, 7, 9])
print('Print random number from array')
print(x)
# Generate random number from array - Use the size parameter
print('Print random number from array using size')
x = random.choice([3, 5, 7, 9], size=(2, 3))
print(x)

# Random Distribution - TODO
