from math import sqrt
from functools import reduce

"""
Question 1: Convert an expression that uses map and filter into an equivalent list comprehension
"""
print('Problem 1')

mylist = [1, 2, 3, 4, 5]
lx = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, mylist)))
print(lx)

# new_list = [expression for item in iterable if conditional ]
lx = [x * x for x in mylist if x % 2 == 1]
print(lx)

"""
Question 2: Convert an expression that uses a list comprehension into equivalent code that uses the map function
and a lambda function
"""
print("\n---Problem 2---")

mylist = [1, 2, 3, 4, 5]
print([2 ** x for x in mylist])

print(list(map(lambda x: 2**x, mylist)))

"""
Question 3: What is the output of the following?
"""
print("\n---Problem 3---")

x = [i**3 for i in range(4)]
print(x)

"""
Question 4: What is the output of the following?
"""
print("\n---Problem 4---")

print(list(filter(lambda a : a % 3==0, [0,1,2,3,4,5,6,7,8,9])))

"""
Question 5: What is the output of the following?
"""
print("\n---Problem 5---")

print(list(map(str,map(lambda x : sqrt(x), [4,9,16,25]))))

"""
Question 6: What is the output of the following?
"""
print("\n---Problem 6---")

x = [5*3 for i in range(4)]
print(x)

"""
Question 7: What is the output of the following?
"""
print("\n---Problem 7---")

print(reduce(lambda x, y: x//2 + y//2, [16, 15, 14, 13]))

"""
Question 8:  Convert an expression that uses a list comprehension into equivalent code that uses the map function
"""
print("\n---Problem 8---")

lx = [sqrt(y) for y in range(5)]
print(lx)

lx = list(map(sqrt, range(5)))
print(lx)

"""
Question 9:  Convert an expression that uses a list comprehension into equivalent code that uses the map function
"""
print("\n---Problem 9---")

names = ['Mukesh', 'Roni', 'Chari']

ages = [24, 50, 18]
for i, (name, age) in enumerate(zip(names, ages)):
    if i == 1:
        print(i, name, age)

"""
Question 10:  What will it print?
"""
print("\n---Problem 10---")

stocks = ['AAPL', 'TSLA']
prices = [130.19, 111.7]

new_dict = {stocks:prices for stocks, prices in zip(stocks, prices)}
print(new_dict)