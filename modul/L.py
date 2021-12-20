n = int(input())
a = list(map(int, input().split(' ')))
if len(a) != n:
    raise Exception('n != list len')
for i in range(n):
    if a[i] > 100000:
        raise Exception('nums <100000')
m = int(input())
b = list(map(int, input().split(' ')))
if len(a) != n:
    raise Exception('n != list len')
for j in range(m):
    if b[j] > 100000:
        raise Exception('nums <100000')
c = a+b
c = set(c)
d = list(c)
print(sorted(d))