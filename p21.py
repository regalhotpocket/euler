def amicable_number(n):
    l = sum(m for m in range(1,n) if n%m==0)
    r = sum(m for m in range(1,l) if l%m==0)
    return True if l != r and r == n else False
print(sum(x for x in range(1,10001) if amicable_number(x)))
