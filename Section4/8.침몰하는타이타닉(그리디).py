from collections import deque

n, limit = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = deque(a)
cnt = 0

while a:
    if len(a) == 1:
        cnt += 1
        break
    if a[0] + a[-1] > limit:
        a.pop()
        cnt += 1
    else:
        a.pop()
        a.popleft()
        cnt += 1