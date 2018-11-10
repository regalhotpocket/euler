from math import sqrt
from typing import Generator

def fib():
    a = 0
    b = 1
    yield 1
    while(True):
        yield a+b
        b, a = a+b, b

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2,1+round(sqrt(n))):
        if n % x == 0:
            return False
    return True

#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n: int) -> Generator[int,  None, None]:
    l = [False]*(n+1)
    p = 2
    while p <= n:
        yield p
        for i in range(1,n//p+1):
            l[i*p] = True
        p += 1
        while p <= n and l[p] == True:
            p += 1