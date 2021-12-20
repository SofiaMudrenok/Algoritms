a = [0 for i in range(101)]
n = float(input())
i=0
while i < n:
    a[i]=float(input())
    if a[i] >= 0:
        a[i] += 2
        i += 1
print(a)
