
solutions = []

for x in range(2,1000000):
    y = 0
    z = x
    while z != 0:
        y += (z%10)**5
        z //= 10
    if y == x:
        solutions.append(x)

print(sum(solutions))