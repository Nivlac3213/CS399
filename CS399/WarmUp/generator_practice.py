# fill in this function
def fib():
    a = 1
    b = 2
    yield a
    yield b
    while (1):
        yield (b + a)
        a, b = b, a
        b = b + a


# testing code
import types

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break