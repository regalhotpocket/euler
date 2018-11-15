def ways(n, m=200):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(ways(n-x, x) for x in [200, 100, 50, 20, 10, 5, 2, 1] if x <= m)
print(ways(200))