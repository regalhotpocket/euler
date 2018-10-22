# https://en.wikipedia.org/wiki/Summation

n = 100
sum_of_square = pow(n,3)/3 + pow(n,2)/2 + n/6
square_of_sum = pow(n*(n + 1)/2,2)
print(abs(square_of_sum - sum_of_square))