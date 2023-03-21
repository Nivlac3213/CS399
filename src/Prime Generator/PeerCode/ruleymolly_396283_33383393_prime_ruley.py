# Molly Ruley
# Prime numbers
# Assignment_1 1/26/23


def generate_primes() -> list:
    yield 2
    n = 3
    yield n
    prime_list = [n]
    while True:
        n += 2
        for p in prime_list:
            if n % p == 0:
                break
            # I want this loop to end once it gets to the root of the number (n), but using the below
            # construct does not work. How could I implement it?
            # if p > int((n**0.5))+1:
            # break
        else:
            yield n
            prime_list.append(n)


if __name__ == '__main__':
    for p in generate_primes():
        print(p)
