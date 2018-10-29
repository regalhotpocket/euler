from math import factorial
def dance(n: int)->int:
    return n%10 + dance(n//10) if n != 0 else 0
print(dance(factorial(100)))