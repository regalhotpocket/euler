from math import sqrt, floor
count = 1
triangle_number = 1
while sum(2 for x in range(1,floor(sqrt(triangle_number))) if triangle_number%x == 0) < 500:
    count += 1
    triangle_number += count
print(triangle_number)