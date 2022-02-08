n = int(input())
a = [ list(map(int, input().split())) for _ in range(n) ]
m = int(input())

for i in range(m):
    r, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[r-1].append(a[r-1].pop(0))
    else:
        for _ in range(k):
            a[r-1].insert(0, a[r-1].pop())

lt = 0
rt = n-1
tot = 0
for i in range(n):
    for j in range(lt, rt+1):
        tot += a[i][j]
    if i < n // 2:
        lt += 1
        rt -= 1
    else :
        lt -= 1
        rt += 1

print(tot)