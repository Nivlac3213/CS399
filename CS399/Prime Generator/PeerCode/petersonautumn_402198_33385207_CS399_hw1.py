"""
Prime Number Generator: a program that uses highly optimized generator functions that yield all prime numbers
By: Autumn Peterson
Date: 31 January 2023
"""

import itertools


def prime_gen():
    yield 2
    """generates prime numbers"""
    prime_lst = [2]  # list that prime numbers are stored in and first prime is always 2
    for n in itertools.count(3, 2):  # counts only odds starting at three
        for i in range(2, int(n ** .5) + 1):  # cuts back on number of checks by only checking up to square root of n
            if n % i == 0:
                break
        else:
            prime_lst.append(n)
            yield n  # yields each prime number as it is found


if __name__ == '__main__':
    for p in prime_gen():
        print(p)
