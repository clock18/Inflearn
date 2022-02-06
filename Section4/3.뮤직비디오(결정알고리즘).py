def count(capacity):
    cnt = 1
    tot = 0
    for x in music:
        if tot + x > capacity:
            cnt += 1
            tot = x
        else:
            tot += x
    return cnt

n, m = map(int, input().split())
music = list(map(int, input().split()))

lt = 1
rt = sum(music)
maxMusic = max(music)
res = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if count(mid) <= m and maxMusic <= mid:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
