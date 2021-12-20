from math import gcd
from functools import reduce

m = 1
n = int(input('n = '))
a = list(map(int, input().split(' ')))
if len(a) != n:
    raise Exception('n != list len')
for i in range(n):
    m *= a[i]
b = reduce(gcd, a)
print(m / b)