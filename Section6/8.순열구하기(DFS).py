def DFS(L):
    global cnt
    if L == m :
        for i in range(m) :
            print(res[i], end=' ')
        print()
        cnt += 1
    else :
        for j in range(1, n+1) :
            if ck[j] == 0 :
                ck[j] = 1
                res[L] = j
                DFS(L+1)
                ck[j] = 0

if __name__ == "__main__" :
    n, m = map(int, input().split())
    res = [0] * m
    ck = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)