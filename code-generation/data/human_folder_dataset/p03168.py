from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    n = int(input())
    probabilities = list(map(float, input().split()))

    # dp[i] = P(i heads coins)
    dp = [0.0] * (n//2 + 3)
    dp[0] = 1.0
    for p in probabilities:
        dp[n//2 + 1] += dp[n//2] * p
        for j in range(n//2 + 1)[::-1]:
            dp[j] = dp[j] * (1 - p) + dp[j-1] * p

    print(dp[n//2 + 1])

main()