from a1.hallenbeckgarrett_LATE_401306_33391873_main import prime_numbers as gen_a
from a1.lawsteagan_255849_33388038_Laws_CS399_Assign1 import primes_generator as gen_b
from a1.phantri_276900_33387791_pRIMES import Primes as gen_c
from a1.uhlerskyler_279243_33381622_PrimeNumbers_CS399_UhlerSkyler import find_prime as gen_d
from a1.wallschlaegerjordan_402183_33386716_prime_gen import prime_gen as gen_e

from a1.hancocktaylor_321946_33386522_findPrimes import get_prime as gen_1
from a1.henggelercalvin_272778_33357261_prime_generator_HenggelerCalvin import optimized_prime_generator as gen_2
from a1.mitchelljaxson_320831_33383857_PrimeGenerator import prime_generator as gen_3
from a1.novakmarcello_418008_33362307_nthPrimeGenerator import primeGenerator as gen_4
from a1.petersonautumn_402198_33385207_CS399_hw1 import prime_gen as gen_5
from a1.prawatmuangworamon_404117_33364582_submission import prime_generator as gen_6
from a1.ruleymolly_396283_33383393_prime_ruley import generate_primes as gen_7
from a1.spencercharles_392946_33375353 import prime_gen as gen_8
from assignment1 import prime_generator as gen_9
from assigment1_file import prime_generator as gen_10

from time import process_time

known_prime = (1_000_000, 15485863)
known_prime = (100_000, 1299709)
known_prime = (10_000, 104729)

x = [gen_a, gen_b, gen_c, gen_d, gen_e]  # Restricted Generators
for g in x:
    t0 = process_time()
    prime_generator = g(known_prime[0])
    for k, prime in enumerate(prime_generator, 1):
        if k == known_prime[0]:
            assert prime == known_prime[1]
            prime_generator.close()
    print(g.__module__, process_time() - t0)

x = [gen_1, gen_2, gen_3, gen_4, gen_5, gen_6, gen_7, gen_8, gen_9, gen_10]  # Unrestricted Generators
for g in x:
    t0 = process_time()
    prime_generator = g()
    for k, prime in enumerate(prime_generator, 1):
        if k == known_prime[0]:
            assert prime == known_prime[1]
            prime_generator.close()
    print(g.__module__, process_time() - t0)
