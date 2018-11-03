from itertools import permutations, islice

print(next(islice(permutations("0123456789"), 999999,1000000)))