# Author: Taylor Hancock

import itertools
from time import process_time

""" Using itertools as range does not allow for unending increments,
    and itertools is apparently significantly faster (and looks nicer)
    than an infinite loop.                                              """

""" Note: If you really want speed, you can use a Prime Sieve (probably a wheel sieve), but using one of those
          felt like it was beginning to be...cheaty, since it's not really a generator at that point. Also, if
          you decide to prioritize space over speed, you could recursively call get_prime() rather than maintaining
          a list of all primes. I'm unsure if that would actually break things due to stack overflows, but it's
          certainly an interesting concept. """


# Basics of this function borrowed from the Generators video provided:
def get_prime():
    # Handle the first prime
    yield 2
    prime_cache = []  # Why should this function ever check 2? I'm only checking odds

    # Loop over positive, odd integers
    for n in itertools.count(3, 2):
        is_prime = True

        # Calc square root of n (prevents repeated calculations with each loop)
        sqrt_n = n ** 0.5

        # Loop through each possible prime (odd numbers)
        for val in prime_cache:
            # Only check primality if n is less than the square root of the last prime
            if val > sqrt_n:
                break
            # If n is divisible by a prime, it is not prime
            if n % val == 0:
                is_prime = False
                break
        if is_prime:
            # If n is prime, add it to the cache and yield it
            prime_cache.append(n)
            yield n


if __name__ == "__main__":
    # Test the function
    print("Calculation Started\n")
    dt = []
    for i in range(10):
        t0 = process_time()
        for prime in get_prime():
            # print(prime)
            if prime > 10000000:
                break
        dt.append(process_time() - t0)
        print(f"Took {dt} seconds to find all primes below ten million.")
    print("Calculation Finished\n")
    print(f"Average time: {sum(dt) / len(dt)} seconds")
