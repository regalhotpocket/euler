from shared import sieve_of_eratosthenes

primes = [False]*86162
for p in sieve_of_eratosthenes(86162):
    primes[p] = True
m = 0
ma = 0
mb = 0
def prime_count(a, b):
    c = 0
    v = c**2 + a*c + b
    while primes[v] == True:
        c += 1
        v = c**2 + a*c + b
    return c
for a in range(-999,1000):
    for b in range(-1000,1001):
        c = prime_count(a,b)
        if c > m:
            ma = a
            mb = b
            m = c
print(ma*mb)