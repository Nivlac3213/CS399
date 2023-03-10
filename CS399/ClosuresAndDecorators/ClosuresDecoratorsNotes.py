"""
Notes for Closesures and Decorators
also compare to closures to Decorators
"""

# -----------------
# Generators Review
# -----------------

# Generators are like functions but bounce between the generator and
# the primary cod and can infinitly produce their results


# Generators Example
def fib():
    a = 1
    b = 2
    yield a
    yield b
    while 1:
        yield b + a
        a, b = b, a
        b = b + a


# Generate the first 10 prime numbers
counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break

# -----------------
# Closures
# -----------------
"""
Closures store a function in ar particular state/ Environment.
A closure allows the function to access captured variables through the
closure's reference to them

A closure is an inner func that remember and has access to the variables
of the scope that it was created (outer_func)
"""


# Example
def outer_func(msg:str):
    message = msg

    def inner_func():
        print(message)

    # returns the inner function, no executed
    return inner_func


my_func = outer_func('text')
my_func()

# -----------------
# Decorators
# -----------------


def decorator_function(original_function):
    """ This decorator function becomes a decorator"""
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

#
# The following two uses are functionally the same
#


# ----- 1 -----
@decorator_function
def display():
    print('display function ran')

display()

# ----- 2 -----
def display1():
    print('Display1 function ran')

decorated_display = decorator_function(display1)
decorated_display()

#
# Decorators Class Example
#

# Decorators functions are more often used than decorators classes

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_class
def display2():
    print('display2 function ran')


display2()


# -----------------
# Practical Examples
# -----------------

# Logging Decorator
def my_logger(original_function):
    import logging
    logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs}')
        return original_function(*args, **kwargs)
    return wrapper


# Timing Decorator
def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_function.__name__} ran in: {t2} sec')
        return result
    return wrapper


"""
Built in decorators

There are built in decorators for caching results
Cahing techniques:
FIFO
LIFO
LRU -> least frequenty used
MRU -> rmost requenty used

finn.io for stock service

"""
from functools import lru_cache


# Can also use @cache
@lru_cache(maxsize=128)
def fibo(n: int) -> int:
    """
    :return: n-th fibonacci number
    """
    return n if n<2 else fibo(n - 1) + fibo(n - 2)


