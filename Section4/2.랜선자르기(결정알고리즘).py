def count(len):
    tmp = 0
    for x in line:
        tmp += x // len
    return tmp

k, n = map(int, input().split())
line = []
largest = 0

for i in range(k):
    a = int(input())
    line.append(a)
    largest = max(largest, a)

lt = 1
rt = largest
res = 0

while lt <= rt :
    mid = (lt+rt) // 2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)