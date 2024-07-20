def main():
    h, n = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    amax = max(a for a, b in ab)
    dp = [0] + [0] * (h + amax)
    for i in range(1, h + 1):
        dp[i] = min(dp[i - a] + b for a, b in ab)
    print(dp[h])


if __name__ == '__main__':
    main()
