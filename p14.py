from collections import defaultdict
cache = defaultdict(int)
def sequence_len(n: int) -> int:
    if n == 1:
        return 1
    elif cache[n] == 0:
        result = (sequence_len(n/2) if n%2 == 0 else sequence_len(3*n+1))
        cache[n] = result+1
    return cache[n]
largest_len = 0
largest_start = 0
for n in range(1,1000000):
    l = sequence_len(n)
    if l > largest_len:
        largest_start = n
        largest_len = l
print(largest_start)