# 1. a^2 + b^2 = c^2
# 2. a + b + c = 1000
# c = 1000 - a - b
# a^2 + b^2 = (1000 - a - b)^2
# a^2 + b^2 = a^2 + 2ab - 2000a + b^2 - 2000b + 1000000
# a^2 + b^2 = a^2 + 2ab - 2000a + b^2 - 2000b + 1000000
# b = 1000(a-500)/(a-1000)
# a^2 + (1000(a-500)/(a-1000))^2 = c^2
# c = sqrt(a^2 + (1000(a-500)/(a-1000))^2)
# 1000 = sqrt(a^2 + (1000(a-500)/(a-1000))^2) + 1000(a-500)/(a-1000) + a
from math import sqrt
for a in range(1,1000):
    b = 1000*(a-500)/(a-1000)
    c = sqrt(a**2 + (1000*(a-500)/(a-1000))**2)
    if a + b + c == 1000 and b.is_integer() and c.is_integer() and a < b and b < c:
        print(a, b, c, a*b*c)