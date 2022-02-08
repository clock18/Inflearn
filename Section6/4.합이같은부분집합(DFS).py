import sys
sys.stdin = open("input.txt",'r')

def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n : # 0번 인덱스부터 사용했기 때문에 n이되면 종료
        if sum == (total-sum):
            print('yes')
            sys.exit(0)
    else :
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")