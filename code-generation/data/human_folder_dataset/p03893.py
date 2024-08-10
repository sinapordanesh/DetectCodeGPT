def main():
    X = int(input())
    dp = [0] * (X+1)
    dp[0] = 2
    for i in range(X):
        dp[i+1] = dp[i] * 2 + 2
    print(dp[X])


if __name__ == "__main__":
    main()
