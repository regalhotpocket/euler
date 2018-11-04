#https://www.mathblog.dk/project-euler-26-find-the-value-of-d-1000-for-which-1d-contains-the-longest-recurring-cycle/
def find_cycle(d: int, t: list)->int:
    n = 1
    c = 0
    while n%d != 0 and c <= d+1: 
        if t[n%d] > 0:
            return c - t[n%d]
        t[n%d] = c
        c += 1
        n = 10*(n%d)
    return 0
m = 0
i = 0
for x in range(2,1000):
    r = find_cycle(x,[-1]*x)
    if r > m:
        i = x
        m = r
print(i)