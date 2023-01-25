import itertools
from time import process_time
from math import sqrt

def prime_generator():
    """
    Prime number generator from the lesson video used as performance baseline
    :return: int prime numbers
    """
    # Handle First Prime Number
    yield 2
    prime_cache = [2]

    # Loop over positive odd integers
    for n in itertools.count(3, 2):
        is_prime = True

        # See if any prime number divides n
        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break

        # Yield if prime
        if is_prime:
            prime_cache.append(n)
            yield n


def optimized_prime_generator():
    """
    Generates Prime Numbers (Optimized)
    :return: int prime numbers
    """
    # Handle First Prime Number
    yield 2

    # Don't add 2 to prime_cache, comparing any prime to 2 is worthless because they are all odd numbers
    prime_cache = []

    # Loop over positive odd integers
    for n in itertools.count(3, 2):
        is_prime = True

        # Mathematically all primes are mod6 = 5 or 1, check before looping
        if (n % 6 == 1) or (n % 6 == 5):

            # See if any prime number divides n
            for p in prime_cache:

                # Only check up to the sqrt(n)
                if sqrt(n) < p:
                    break
                if n % p == 0:
                    is_prime = False
                    break

            # Yield if prime
            if is_prime:
                prime_cache.append(n)
                yield n


if __name__ =='__main__':

    """
    Run Optimized Generator
    """
    # Generate all primes under 500k
    t0 = process_time()
    for p in prime_generator():
        if p < 500000:
            print(p)
        else:
            break
    dt0 = process_time() - t0

    """
    Run Optimized Generator
    """
    t1 = process_time()
    # Generate all primes under 1 Million
    for p in optimized_prime_generator():
        if p < 1000000:
            print(p)
        else:
            break
    dt1 = process_time() - t1

    # Print Processing Times
    # print(f"Processing: {dt0} seconds")
    print(f"Optimized Processing: {dt1} seconds")