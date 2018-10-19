from math import floor, ceil

def find_length(n: int) -> int:
    count = 0
    while n > 1:
        count += 1
        n /= 10
    return count
def check(n: int) -> bool:
    l = find_length(n)
    half = floor(n / 10**ceil(l/2))
    rev = 0
    for i in range(floor(l/2)):
        rev += n%10*10**(floor(l/2)-i-1)
        n   =  floor(n/10)
    return True if half == rev else False
def largest_palindrome_product(digits: int) -> int:    
    for x in reversed(range(1,10**digits)):
        for y in reversed(range(1,10**digits)):
                if check(x*y):
                    return(x, y, x*y)

print(largest_palindrome_product(3))