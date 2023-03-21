from math import sqrt
from itertools import count


def find_prime(n):
    # 2 is only even prime number, and 3 is first odd prime number. Throw 5 in for good measure.
    global primes
    primes = [3, 5]
    yield 2
    yield 3
    yield 5
    # Start at 7, and increment by 2, since all primes after 3 are odd. "The AI came up with this comment" -AI
    for x in count(7, 2):
        prime = True
        for p in primes:
            if p > sqrt(x):  # If it is not divisible by any number less than the square root, it is prime.
                break
            if x % p == 0:
                prime = False
                break
        if prime:
            primes.append(x)
            yield x


if __name__ == '__main__':

    number = int(input("What n'th prime number do you want? "))
    primes = []

    for f in find_prime(number):
        print(f)
        if len(primes) + 1 == number:
            break
