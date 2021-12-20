n=int(input())
x = [0 for _ in range(n)]
counter = 0
i = 0
while i < n:
    x[i]=float(input())
    i += 1
first = x[0]
i = 0
while i < n - 1:
    min = i
    j = i + 1
    while j < n:
        if x[j] < x[min]:
            min = j
        j += 1
    if (x[i] == first or x[min] == first) and x[i] != x[min]:
        counter += 1
    x[i], x[min]=x[min], x[i]
    i += 1
print(counter)
