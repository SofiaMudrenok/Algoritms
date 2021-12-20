n=float(input())
max = 0
i = 0
while i < n:
    a = float(input())
    if abs(a) > max:
        max = abs(a)
    i += 1
print(max)
