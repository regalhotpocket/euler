from math import sqrt

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