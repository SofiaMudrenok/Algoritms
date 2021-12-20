n = int(input('n: '))
l1 = list(map(int, input().split(' ')))
if len(l1) != n:
    raise ValueError
m = int(input('m: '))
l2 = list(map(int, input().split(' ')))
if len(l2) != m:
    raise ValueError
res = []
for i in l1:
    if i not in l2:
        res.append(i)
print(len(res))
print(*res)