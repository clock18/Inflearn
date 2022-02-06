n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))

body.sort(reverse=True)

cnt = 0
largest = 0

for a,b in body:
    if b > largest:
        largest = b
        cnt += 1

print(cnt)