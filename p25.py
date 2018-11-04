from itertools import takewhile
from shared import fib

c = sum(1 for y in takewhile(lambda x: x < 10**999, fib()))+1 #unfixable off-by-one, kill me
print(c)