res = 0
a = list(map(int, input('0>num<9').split(' ')))
for i in range(10):
    res += a.count(i)//2
print(res)