from shared import is_prime
from math import floor, sqrt

def find_factors(n: int) -> list:
    result = []
    x = 2
    while(n > 1):
        if n % x == 0 and is_prime(x):
            result.append(x)
            n /= x
            x = 2   
        else:
            x += 1
    return result

def range_divisable(n: int) -> int:
    a = [0] * (n+2)
    for x in range(1,n+1):
        b = [0] * (n+2)
        f = find_factors(x)
        for y in f:
            b[y] += 1
        for i in range(n+2):
            a[i] = max(a[i], b[i])
    result = 1
    for i in range(n+2):
        if a[i] != 0:
            result *= i**a[i]
    return result

print(range_divisable(20))

# https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p005.py
# this solution is so much better xd