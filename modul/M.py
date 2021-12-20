count1 = 0
count2 = 0
while True:
    n = int(input())
    if 1 > n > 100:
        print('1>num<200')
    else:
        break
a = list(map(int, input().split(' ')))
for i in range(n):
    if -50 > a[i] > 50:
        raise Exception('num must be >-50 and <50')
for i in range(n):
    if a[i] > 0:
        count1 += 1
    else:
        count1 = 0
    if count1 > count2:
        count2 = count1
print(count2)