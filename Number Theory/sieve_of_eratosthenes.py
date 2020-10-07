"""
    To efficiently calculate prime number upto
    a given number n.
"""


def sieve(number):
    primes = [1] * (number + 1)
    primes[0] = primes[1] = 0
    i = 2
    while i * i <= number:
        for j in range(i * 2, number + 1, i):
            primes[j] = 0
        i += 1
    prime_list = []
    for i in range(number + 1):
        if primes[i]:
            prime_list.append(i)
    return prime_list


n = int(input())
print(sieve(n))
