n = int(input())
a = list(map(int, input().split()))
res = ''
lt = 0
rt = n-1
line = []
tot = 0

while lt <= rt:
    if a[lt] > tot :
        line.append((a[lt], 'L'))
    if a[rt] > tot :
        line.append((a[rt],'R'))
    line.sort()
    if len(line) == 0 :
        break
    else:
        res = res + line[0][1]
        tot = line[0][0]
        if line[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    line.clear()
print(len(res))
print(res)
