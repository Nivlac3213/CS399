"""
Jaxson Mitchell
CS 399
The goal of this is to create a generator that will generate primes
extremely efficiently.
"""

"""
This was my initial method, but it was super inefficient that is was completely incapable of solving up to 
the 50000th digit in under 20 minutes.
# Method 1 Uses the import itertools.
import itertools  # Imported so it can generate arbitrarily high numbers.


def prime_generator_method_2():  # Generator of primes
    yield 2  # First prime

    prime_list = []  # Creates a list containing odd primes this excludes the prime = 2 since It's unnecessary to check
    # due to the itertools count only going over odd integers when checking whether an integer is prime.

    # Loop over positive, odd integers therefore we do not need to check the n % 2 == 0 case
    for n in itertools.count(3, 2):
        is_prime = True  # Starts as true until shown that n % p == 0.

        # Check to see if any prime number divides n, the only ones that it needs to check are the prime numbers that
        # Are within 3-sqrt(n), so I create a list comprehension here to generate the list you need to check quicker.
        check_list = [x for x in prime_list if x <= int(n ** (1/2) + 1)]

        for p in check_list:  # Iterates over the condensed list instead of the full list.
            if n % p == 0:  # p is a multiple of n
                is_prime = False
                break

        if is_prime:  # if n % p was not 0 for all the primes checked, then the number must be prime.
            prime_list.append(n)  # It appends the value to the list, this kind of ruins the point of the generator
            # since it takes up memory...
            yield n  # Yields n as a prime number.
"""


def prime_check(prime_cache: list, p):
    """
    :param prime_cache: Cache of primes that you are looking over
    :param p: The prime number you are checking.
    :return: Returns whether that prime number is divisible (boolean) as well as its divisor if it is.
    """
    check_list = [x for x in prime_cache if x <= int(p ** (1 / 2) + 1)]
    for i in check_list:  # Iterates over the condensed list instead of the full list.
        if p % i == 0:  # p is a multiple of n
            return i
    return None


# Method 2
def prime_generator():  # Generator of primes, using similar method to sieve of Eratosthenes which takes up less memory
    """
    This method creates a range of values N in size as well as an array of True boolean values. A number corresponds to
    a true value within the array if it is prime. Otherwise, it is not prime. I wanted to use the sieve of Eratosthenes
    since the method is extremely efficient in computing primes, but it was memory intensive and ruined the point of the
    generator, therefore this is a modified version of this algorithm that looks at a specific window of size N.
    You have a cache of primes, from this cache of primes you will see if the given number is prime or not using the
    method given in method 1 where it looks until the value is larger than its square root. If it is prime, it is
    added to the prime cache, and it continues.
    The only difference is that if a number X is composite, lets say by the number 3,
    it will subsequently take out every other value from the list of the form X + 3k where k is a positive integer, and
    it will skip checking all of those values. This gets to be more effective with a higher N value, but the trade-off
    is that the list size needed is 2 * N + #primes which will take up a lot of memory at extremely high prime values.
    """
    N = 500000  # Size of each list you will be looking at, can't be too large since it would make the code crash :(
    yield 2

    prime_cache = [2]  # Initializes a list containing all the primes.
    n = 0  # First n-value which will iterate up indefinitely.

    while True:  # Starts the generator to continue indefinitely

        number_range = range(3 + n * N, 3 + (n + 1) * N, 2)  # Range of numbers you look through in an iteration
        # Looks through 3, 5, ..., N + 1 at first.

        prime_check_list = [True for _ in range(N)]  # True corresponds to the value being prime.

        for i in range(int(N / 2)):
            # Iterates over the first range of values.

            if prime_check_list[i]:  # If it's true, it's currently checked as prime, doesn't necessarily mean it is.
                divisor = prime_check(prime_cache, number_range[i])  # Goes through a check to see if its prime.

                # Whether the number is prime or composite
                if divisor is None:  # If there are no divisors, it must be prime.
                    prime_cache.append(number_range[i])
                    yield number_range[i]
                else:  # This shows that it is composite
                    steps = int((number_range[-1] - number_range[i]) // divisor) + 1
                    # The number of steps until you would go outside the list you are checking.

                    for k in range(steps):  # Iterates over all steps within list.
                        prime_check_list[i + divisor * k] = False
        n += 1  # Goes to the next values.


if __name__ == '__main__':
    from time import process_time

    known_prime = (50_000, 611953)
    t0 = process_time()
    primes = prime_generator()
    for k, prime in enumerate(primes, 1):
        if k == known_prime[0]:
            print(f"The {k:,}-th prime number is {prime}")
            assert prime == known_prime[1]
            primes.close()
    print(process_time() - t0)
