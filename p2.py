from shared import fib
from itertools import filterfalse, takewhile
print(sum(filterfalse(lambda y:y%2==0, takewhile(lambda x: x < 4000000, fib()))))