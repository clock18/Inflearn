def check(a):
    for i in range(9):
        sum1 = [0] * 10
        sum2 = [0] * 10
        for j in range(9):
            sum1[a[i][j]] = 1
            sum2[a[j][i]] = 1
        if sum(sum1) != 9 or sum(sum2) != 9 :
            return False

    for i in range(3):
        for j in range(3):
            sum3 = [0] * 10
            for k in range(3):
                for l in range(3):
                    sum3[a[i*3+k][j*3+l]] = 1
            if sum(sum3) != 9:
                return False

    return True

a = [ list(map(int, input().split())) for _ in range(9)]
if check(a):
    print('YES')
else :
     print('NO')