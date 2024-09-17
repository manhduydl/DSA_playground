# 6 7
# 1 6 9 13 18 18
# 2 3 8 13 15 21 25

n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

i, j = 0, 0
res = []
while i < n and j < m:
    if a[i] <= b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1

while i < n:
    res.append(a[i])
    i+=1

while j < m:
    res.append(b[j])
    j+=1

print(res)