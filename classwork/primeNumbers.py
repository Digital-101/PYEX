# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:55:33 2024

@author: dop24
"""

#Prime 

def is_prime(num):
    """ Function to check if a number is prime """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    """ Function to find the first n prime numbers """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Finding the first 200 prime numbers
first_200_primes = first_n_primes(200)

# Printing the first 200 prime numbers
for i, prime in enumerate(first_200_primes, start=1):
    print(f"Prime {i}: {prime}")




def is_prime2(num):
    """ Function to check if a number is prime """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# List to store prime numbers between 1 and 200
prime_numbers = []

# Loop through numbers from 1 to 200 and check for primes
for num in range(1, 201):
    if is_prime2(num):
        prime_numbers.append(num)

# Printing the prime numbers found
print("Prime numbers between 1 and 200:")
print(prime_numbers)


# Using Nested For Loops
def find_primes_between(start, end):
    prime_numbers2 = []
    
    for num in range(start, end + 1):
        if num > 1:
            is_prime3 = True
            for i in range(2, int(num**0.5) +1 ):
                if num % i == 0:
                    is_prime3 = False
                    break
            if is_prime3:
                prime_numbers2.append(num)
    
    return prime_numbers2

#Finding prime numbers between 1 and 200
prime_numbers2 = find_primes_between(1, 200)

#Printing the prime numbers found
print("Prime numbers between 1 and 200:")
print(prime_numbers2)