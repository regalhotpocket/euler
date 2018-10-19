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
    d = sum([9*10**a for a in range(digits)])
    return max([x * y for x in range(d) for y in range(d) if check(x*y)])

print(largest_palindrome_product(3))