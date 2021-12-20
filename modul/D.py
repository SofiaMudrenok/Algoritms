k = 0
s = 0
n = float(input())
i = 0
while i < n:
    x=float(input())
    if x > 0:
            s += x
            k += 1
    i += 1
if s > 0:
    print(s / k)
else:
        print("Not Found")
