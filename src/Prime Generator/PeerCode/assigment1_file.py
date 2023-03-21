"""
Warmup: Generator assignment
"""
from time import process_time


def prime_generator():
    yield 2
    cache_file = "primes.txt"

    with open(cache_file, "a+") as prime_cache:
        if prime_cache.tell() == 0:  # file is empty .. initializing cache_file with next prime after 2
            prime_cache.write("3\n")
        prime_cache.seek(0)
        for p in prime_cache:  # before doing any work, reuse previous results
            n = int(p)
            yield n

        while True:
            n += 2
            sqrt_n = round(n ** 0.5)

            try:
                prime_cache.seek(0)
                for p in prime_cache:
                    p = int(p)
                    if n % p == 0:
                        break
                    if p > sqrt_n:
                        prime_cache.write(f"{n}\n")
                        yield n
                        break
            except IOError as ioe:
                print(f"Sh!t, there was an i/o problem {ioe}")
                exit(1)
            except GeneratorExit:
                print("Properly closing the cache file")
                prime_cache.close()
                return


if __name__ == "__main__":
    known_prime = (1_000_000, 15485863)
    # known_prime = (1_000, 7919)
    # known_prime = (100_000, 1299709)
    # known_prime = (100, 541)
    t0 = process_time()
    primes = prime_generator()
    for k, prime in enumerate(primes, 1):
        if k == known_prime[0]:
            print(f"The {k:,}-th prime number is {prime}")
            assert prime == known_prime[1]
            primes.close()
    print(process_time() - t0)
