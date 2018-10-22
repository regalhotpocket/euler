from shared import is_prime

count = 0
cur = 0
n = 10001

while count < n:
    cur += 1
    if is_prime(cur) == True:
        count += 1 
print(cur)