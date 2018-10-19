from math import sqrt

def is_prime(n: int) -> bool:
    for x in range(2,1+round(sqrt(n))):
        if n % x == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    for x in reversed(range(2,1+round(sqrt(n)))):
        if n%x == 0 and is_prime(x):
            return x

print(largest_prime_factor(600851475143))
