"""
Name: Jordan Wallschlaeger
Create a generator that will generate all prime numbers between 2 and (limit)
"""


def prime_gen(n):
    primes = [2]
    for i in range(3, n + 1, 2):  # iterates through all the odd numbers from 0 to (limit)
        for j in range(2, int(i ** 0.5) + 1):  # equation to see if number is prime
            if i % j == 0:
                break
        else:
            primes.append(i)
    yield primes


if __name__ == '__main__':
    limit = 1000000

    prime_list = prime_gen(limit)
    print(list(prime_list)[0][-1])
