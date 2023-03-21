# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:08:56 2023

@author: Tri_P

Reviewer: Calvin Henggeler

"""
from time import process_time

# Using just purely dividing by all previous primes and iterating through odds
t0 = process_time()
def Primes(x):
    primes = [2]
    yield primes[0]
    
    for n in range(primes[-1]+1, x+1, 2):
        prime = True    
        for p in primes:
            if n % p == 0:
                prime = False
                break
        
        if prime:
            primes.append(n)
            yield n

print(list(Primes(160000))[-1])
dt = process_time() - t0
print(f"Processing: {dt:0.5f} seconds")
t0 = process_time()


# Using Sieve of Eratosthenes
def Primes(x):
    lst = list(range(2,x+1)) # List of all numbers we want
    prime = [True for i in range(x+1)]
    
    p = 2
    while (p**2 <= x):
        if prime[p] == True:
            for i in range(p**2, x+1, p):
                prime[i] = False
        p += 1
    
    for i in range(2,x+1):
        if prime[i]:
            yield i
            
print(list(Primes(160000))[-1])
dt = process_time() - t0
     
print(f"Processing: {dt:0.5f} seconds")
                    