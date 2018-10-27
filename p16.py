n = 2**1000
r = 0
while(n > 1):
    r += n%10
    n = n//10
print(r)