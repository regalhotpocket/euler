from math import sqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2,1+round(sqrt(n))):
        if n % x == 0:
            return False
    return True