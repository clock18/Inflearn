N = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/N)
min = 2147000000

for idx, x in enumerate(a):
    std = abs(avg-x)
    if std < min:
        min = std
        score = x
        res = idx + 1
    elif std == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)


