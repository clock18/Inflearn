n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
cnt = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        cnt.append(a[p1])
        p1 += 1
    else:
        cnt.append(b[p2])
        p2 += 1

if p1 < n:
    cnt = cnt + a[p1:]
if p2 < m:
    cnt = cnt + b[p2:]

for x in cnt :
    print(x, end=' ')