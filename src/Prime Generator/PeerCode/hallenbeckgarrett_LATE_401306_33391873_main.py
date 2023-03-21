def prime_numbers(count):
    #  deal with 2 first primes
    yield 2
    prime_count = 1
    if count > 1:
        yield 3
        prime_count += 1
    increment_2_or_4 = True
    num = 5
    # all primes except 2 and 3 can be expressed as 6n +or- 1
    # so it would go from 5 to 7 then 11 to 13
    # https://math.stackexchange.com/questions/895992/6n1-and-6n-1-prime-format
    while prime_count < count:
        for i in range(5, int(num ** 0.5) + 1, 2):  # once you go past the square root you start repeating factors
            if num % i == 0:
                break
        else:
            prime_count += 1
            yield num
        # using a bool is faster than doing a check like if (num+1)%6==0
        if increment_2_or_4:
            num += 2
            increment_2_or_4 = False
        else:
            num += 4
            increment_2_or_4 = True


if __name__ == "__main__":
    for g in enumerate(prime_numbers(100)):
        print(f"{g[0]}: {g[1]}")
