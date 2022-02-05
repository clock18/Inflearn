a = [ list(map(int, input().split())) ]
cnt = 0

for i in range(3):
    for j in range(7):
        res = a[j][i:i+5]
        if res == res[::-1]:
            cnt += 1

        for k in range(2):
            if a[i+k][j] != a[i+4-k][j]:
                break
        else:
            cnt += 1

print(cnt)