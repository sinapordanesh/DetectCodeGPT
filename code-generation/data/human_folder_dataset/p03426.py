def main():
    H,W,D = map(int,input().split())
    N = H*W
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    places = [0] * (H * W + 1)
    for i in range(H):
        for j in range(W):
            places[A[i][j]] = (i,j)
    dp = [0] * (N+1)
    for i in range(D+1,N+1):
        y1,x1 = places[i-D]
        y2,x2 = places[i]
        dp[i] = dp[i-D]+abs(x1-x2)+abs(y1-y2)
    

    Q = int(input())
    queries = []
    ans = []
    for i in range(Q):
        l,r = map(int,input().split())
        ans.append(dp[r] - dp[l])
    print('\n'.join(map(str,ans)))
main()
