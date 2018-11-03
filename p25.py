from itertools import takewhile
def fib():
    a = 0
    b = 1
    yield 1
    while(True):
        yield a+b
        b, a = a+b, b
c = sum(1 for y in takewhile(lambda x: x < 10**999, fib()))+1 #unfixable off-by-one, kill me
print(c)