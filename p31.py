# https://projecteuler.net/problem=31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
# Expected value: 73682
# https://en.wikipedia.org/wiki/Change-making_problem

from timeit import timeit

def method1():
    def ways(n, m=200):
        if n == 0:
            return 1
        if n < 0:
            return 0
        return sum(ways(n-x, x) for x in [200, 100, 50, 20, 10, 5, 2, 1] if x <= m)
    print(ways(200))
def method2():
    ways = [0]*201
    ways[0] = 1
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for change in range(coin, 201):
            ways[change] += ways[change-coin]
    print(ways[200])
print("method1: ", timeit(method1, number=1))
print("method2: ", timeit(method2, number=1))