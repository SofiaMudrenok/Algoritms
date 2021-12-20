lst = list(map(int, input().split(' ')))
seq = list(range(1, lst[0]+1))
a = lst[1]
b = lst[2]
c = lst[3]
d = lst[4]
print(seq[:a-1:] + list(reversed(seq[a-1:b:])) + seq[b:c-1:] + list(reversed(seq[c-1:d:])) + seq[d::])