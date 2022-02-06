def count(mid):
    cnt = 1
    ep = a[0]
    for i in range(1, n):
        if a[i] - ep >= mid:
            cnt += 1
            ep = a[i]
    return cnt

n, c = map(int, input().split())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
a.sort()
lt = 1
rt = max(a)

while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
