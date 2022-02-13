def DFS(L, s) :
    global cnt
    if L == m :
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1
    else :
        for j in range(s, n+1):
            res[L] = j
            DFS(L+1, j+1)

if __name__  == "__main__" :
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)