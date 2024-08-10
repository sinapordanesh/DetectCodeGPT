import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7

def main():
    string = input().strip()
    n = len(string)
    dp = [[0, 0, 0, 0] for _ in range(n + 1)]
    dp[0][0] = 1
    for i, s in enumerate(string):
        if s == "A":
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1] + dp[i][0]
            dp[i + 1][2] = dp[i][2]
            dp[i + 1][3] = dp[i][3]
        elif s == "B":
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = dp[i][2] + dp[i][1]
            dp[i + 1][3] = dp[i][3]
        elif s == "C":
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = dp[i][2]
            dp[i + 1][3] = dp[i][3] + dp[i][2]
        else:
            dp[i + 1][0] = 3 * dp[i][0]
            dp[i + 1][1] = 3 * dp[i][1] + dp[i][0]
            dp[i + 1][2] = 3 * dp[i][2] + dp[i][1]
            dp[i + 1][3] = 3 * dp[i][3] + dp[i][2]
        for j in range(4):
            dp[i + 1][j] %= MOD
    print(dp[-1][-1] % MOD)
    
main()