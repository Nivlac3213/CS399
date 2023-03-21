"""
Warmup: Generator assignment
"""
from math import sqrt


def prime_generator():
    yield 2
    yield 3
    n, prime_cache = 3, [3]
    while True:
        n += 2
        sqrt_n = round(sqrt(n))
        for p in prime_cache:
            if n % p == 0:
                break
            if p > sqrt_n:
                yield n
                prime_cache.append(n)
                break


if __name__ == "__main__":
    from time import process_time

    known_prime = (1_000_000, 15485863)
    known_prime = (1_000, 7919)

    t0 = process_time()
    primes = prime_generator()
    for k, prime in enumerate(primes, 1):
        if k == known_prime[0]:
            print(f"The {k:,}-th prime number is {prime}")
            assert prime == known_prime[1]
            primes.close()
    print(process_time() - t0)
