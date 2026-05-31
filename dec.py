# Trying to understand decorators
# This is a basic example of a decorator. The `my_decorator` function takes
# another function as an argument and defines a wrapper function that adds
# some behavior before and after the original function is called. The
# `@my_decorator` syntax is a shorthand for applying the decorator to the
# `say_hello` function.

def my_decorator(some_fun):
    def wrapper():
        print("Something is happening before the function is called.")
        some_fun()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


if __name__ == "__main__":
    say_hello()
