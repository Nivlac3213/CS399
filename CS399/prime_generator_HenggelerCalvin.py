import itertools
from time import process_time, sleep

# ********************* Original Baseline Prime Generator ********************

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

# ******************** Optimized Prime Generator ********************

def optimized_prime_generator():
    """
    Generates Prime Numbers (Optimized)

    Found the rules about the 5 and 1 modulus in an article about primes, and
    saw the n < p*p optimization in a youtube comment.

    :return: int prime numbers
    """
    # Handle First Prime Number
    yield 2
    yield 3

    # Don't add 2 to prime_cache, comparing any prime to 2 is worthless because
    # they are all odd numbers
    prime_cache = []

    # Loop over positive odd integers
    for n in itertools.count(3, 2):
        is_prime = True

        # Mathematically all primes above 3 are mod6 = 5 or 1, check condition
        # before checking for primeness
        if (n % 6 == 1) or (n % 6 == 5):

            # See if any prime number divides n
            for p in prime_cache:

                # Only check up to the sqrt(n)
                if n < p*p:
                    break
                if n % p == 0:
                    is_prime = False
                    break

            # Yield if prime
            if is_prime:
                prime_cache.append(n)
                yield n


# ---------------------------------------------------------------------------
#                   ************ Main Program ************
# ---------------------------------------------------------------------------
if __name__ == '__main__':

    #
    # Testing the Optimized Generator
    #
    known_prime = (100_000, 1_299_709)  # Tuple representing a known prime number
    t2 = process_time()

    # 'primes' encapsulates all prime numbers
    primes = optimized_prime_generator()
    for k, prime in enumerate(primes, 1):
        if k == known_prime[0]:
            assert prime == known_prime[1]
            print(f"Prime Generator Test Passed: The {k:_}-th prime number is {prime}")
            primes.close()
            sleep(2)
    print(f'Test process time: {process_time() - t2} seconds')

    #
    # Set max Values for generators to generate primes under
    #
    baseline_generator_max  = 100_000    # 100k
    optimized_generator_max = 1_000_000   # 1M

    #
    # Run original (baseline) Generator
    #
    print('Begin Baseline Generator')
    sleep(2)
    t0 = process_time()
    for p in prime_generator():
        if p < baseline_generator_max:
            print(p)
        else:
            break
    dt0 = process_time() - t0
    print('End of Baseline Generator')

    #
    # Run Optimized Generator
    #
    print('Begin Optimized Generator')
    sleep(2)
    t1 = process_time()
    for p in optimized_prime_generator():
        if p < optimized_generator_max:
            print(p)
        else:
            break
    dt1 = process_time() - t1

    from time import process_time

    #
    # Print Processing Times
    #
    print(f"Baseline Processing:    {dt0} seconds to generate primes under {baseline_generator_max}")
    print(f"Optimized Processing:   {dt1} seconds to generate primes under {optimized_generator_max}")
