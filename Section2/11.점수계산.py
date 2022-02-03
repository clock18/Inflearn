n = int(input())
a = list(map(int, input().split()))
cnt = 0
sum = 0

for x in a:
    if x == 1:
        cnt +=1
        sum += cnt
    else:
        cnt = 0

print(sum)