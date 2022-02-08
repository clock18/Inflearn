def DFS(x):
    if x == n+1 :
        for i in range(1, n+1):
            if ck[i] == 1 :
                print(i, end=' ')
        print()
    else :
        ck[x] = 1
        DFS(x+1)
        ck[x] = 0
        DFS(x+1)

if __name__ == "__main__":
    n = int(input())
    ck = [0] * (n+1)
    DFS(1)
