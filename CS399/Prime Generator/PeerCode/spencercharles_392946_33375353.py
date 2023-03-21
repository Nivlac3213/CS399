"""
Author: Charles Spencer
Purpose: Prime Number Generator
Date: 1/28/23
"""
lst = [2, 3]


def prime(x: int):  # Got some erroneous numbers (6 * 4 + 1 = 25), below verifies prime-ness
    global lst
    for n in lst:
        if x % n == 0:
            return False
    return True


def prime_gen():
    yield 2  # , 1  # 2 and 3 do not generate with method below
    yield 3  # , 2
    global lst
    i = 1
    while True:
        t1 = 6 * i - 1  # This is where I found the formula:
        t2 = 6 * i + 1  # https://www.vedantu.com/maths/how-to-find-prime-numbers
        if prime(t1):
            lst.append(t1)
            yield t1  # , lst.index(t1) + 1
        if prime(t2):
            lst.append(t2)
            yield t2  # , lst.index(t2) + 1
        i += 1


if __name__ == '__main__':
    lim = int(input('What is the upper limit: '))
    for num, place in prime_gen():
        if num > lim:
            break
        print(f'prime number {place} is: {num}')
