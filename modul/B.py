n = int(input('n = '))
b = 0
k = 0
a = list(map(int, input().split(' ')))
if len(a)!= n:
    raise Exception('n != list len')
else:
    for i in range(n):
        if a[i] <= 2.5:
            b = a[i]
            k = i
            print('{0} {1}'.format(i, a[i]))
            break
        else:
            print('Not found')
            break