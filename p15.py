#   Two alternate ways to solve this problem
#
#   The number of ways that you can each a location is the sum of ways you can reach it's parent locations.
#   Starting from the last, bottom-right, location, we recursivly try to find the cost of it's parents.
#   We cache results to speed up computation.
from collections import defaultdict
c = defaultdict(int)
def split(x: int, y: int):
    if c[(x,y)] != 0:
        return c[(x,y)]
    if x == 0 and y == 0:
        return 1
    total = 0
    if y > 0:
        total += split(x, y-1)
    if x > 0:
        total += split(x-1, y)
    c[(x,y)] = total
    return total
print(split(20, 20))

#   https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p015.py
#   This is smart solution I found online. If there is a  nxn grid, we will always have n moves down, and n moves to the right.
#   A configureation can be represented by a 2n move sequence DLLD...
#   Each sequcne can be defined by the locations of either all the down moves, or all the up moves.
#   This definition allows us to need only n locations, as the remainding locations will be filled in by the other set of moves.
#   That means that there is combination(40, 20) possible paths
from math import factorial
print(factorial(40)/(factorial(20)*factorial(20)))