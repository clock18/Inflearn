def DFS(L, sum, tsum):
    global res
    if sum + (total - tsum) < res:
        return
    if sum > c :
        return
    if L == n :
        if sum > res:
            res = sum
    else :
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum + a[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = int(input())
    res = -2147000000
    total = sum(a)
    DFS(0, 0, 0)