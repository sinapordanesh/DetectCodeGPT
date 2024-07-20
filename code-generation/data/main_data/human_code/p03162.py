def main():
    N = int(input())
    acts = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        acts.append([a,b,c])
    dp = [[0] * 3 for _ in range(N + 5)]

    dp[0][0] = acts[0][0]
    dp[0][1] = acts[0][1]
    dp[0][2] = acts[0][2]
    for i in range(1,N):
        for j in range(3):
            if j == 0:
                score = max(dp[i-1][1], dp[i-1][2])
            if j == 1:
                score = max(dp[i-1][0], dp[i-1][2])
            if j == 2:
                score = max(dp[i-1][1], dp[i-1][0])
            dp[i][j] = acts[i][j] + score

    print(max(dp[N-1]))



if __name__ == "__main__":
    main()