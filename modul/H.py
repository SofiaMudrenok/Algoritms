from math import gcd
from functools import reduce
n = int(input())
a = list(map(int, input().split(' ')))
if len(a) != n:
    raise Exception('n != list len')
b = reduce(gcd, a)
print(b)