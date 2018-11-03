from itertools import combinations_with_replacement
t = [0]*28124
for x in range(1,28124):
    for y in range(x*2, 28124, x):
        t[y] += x
a = (i for (i,n) in enumerate(t) if i < n)
b = combinations_with_replacement(a,2)
c = set(x+y for x,y in b if x+y <= 28123)
d = set(range(1,28124)).difference(c)
print(sum(d))