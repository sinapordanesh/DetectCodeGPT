import sys
input = sys.stdin.readline
def main():
    N = int(input())
    human = [tuple(map(int, input().split())) for _ in range(N)]

    human.sort(key = lambda x: (x[1]+x[0]))
    inf = 2000000001
    #iからj人乗せた中で最小座布団
    dp = [[inf]*(N+1) for j in range(N+1)]

    for i in range(N+1):
        dp[i][0] = 0

    for i in range(N):
        for j in range(N):
            if dp[i][j] <= human[i][0]:
                dp[i+1][j+1] = min(dp[i][j+1], dp[i][j] + human[i][1])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])

    ans = 0
    for i in range(N+1):
        if dp[N][i] != inf:
            ans = i

    print(ans)

if __name__ == "__main__":
    main()
