## Code by Teagan Laws with assistance from AI ChatGPT
## Commented code would show outputs of prime numbers and execution time

# from time import process_time


def primes_generator(n):
    # Prime number list from 2 to n, the 'all' function checks all the numbers in
    #  the range to see if they aren't divisible by num. If not then it is added
    #  to the list of primes.
    yield [num for num in range(2, n + 1) if all(num % i != 0 for i in range(2, num))]
#    return [num for num in range(2, n+1) if all(num % i != 0 for i in range(2, num))]


# t0 = process_time()
# print(primes_generator(10000))
# print(process_time() - t0)
