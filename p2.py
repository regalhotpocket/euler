x = 1
y = 2
z = 0
while y < 4000000:
    if y % 2 == 0:
        z += y
    x, y = y, x + y
print(z)