import math

n=float(input())
s = 0
q = 0
i = 0
while i < n:
    a =float(input())
    if (math.fmod(a, 6) == 0) and (a > 0):
        q += 1
        s += a
    i += 1
print(q, end = '')
print(' ', end = '')
print(s, end = '')
print("\n", end = '')
