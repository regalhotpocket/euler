from math import floor
from typing import Generator
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def sieve_of_eratosthenes(n: int) -> Generator[int,  None, None]:
    l = [False]*(n+1)
    p = 2
    while p <= n:
        yield p
        for i in range(1,floor(n/p)+1):
            l[i*p] = True
        p += 1
        while p <= n and l[p] == True:
            p += 1
print(sum(sieve_of_eratosthenes(2000000)))