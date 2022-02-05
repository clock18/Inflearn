n = int(input())
a = list(map(int, input().split()))

m = int(input())
for i in range(m):
    r, t, c = map(int, input().split())
    if t == 0:
        for _ in range(c):
            a[r-1].append(a[r-1].pop(0))
    else :
        for _ in range(c):
            a.insert(0, a[r-1].pop())

tot = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e+1):
        tot += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
