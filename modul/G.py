n = int(input())
a = list(map(float, input().split(' ')))
if len(a) != n:
    raise Exception('n != len')
a.insert(0,a.pop())
print(a)