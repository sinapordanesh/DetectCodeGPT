def main():
    mod = 10 ** 9 + 7
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]

    if not m:
        print(0)
        return
    
    mx = [0] * (n + 1)
    mn = [mod] * (n + 1)
    
    for i in range(n):
        if mx[i] > a[i]:
            mx[i + 1] = mx[i]
        else:
            mx[i + 1] = a[i]
    for i in range(n - 1, -1, -1):
        if mn[i + 1] < a[i]:
            mn[i] = mn[i + 1]
        else:
            mn[i] = a[i]
    
    dp = [0] * (n + 1)
    
    dp[1] = 2

    for i in range(1, n):

        ndp = [0] * (n + 1)

        check0 = mx[i + 1] == a[i]
        check1 = mn[i + 1] >= mx[i]
        check2 = mn[i] == a[i]

        if check0:
            if check1:
                for j in range(i + 1):
                    ndp[j + 1] += dp[j]
                    ndp[i - j + 1] += dp[j]

            else:
                for j in range(i + 1):
                    ndp[j + 1] += dp[j]


        else:
            if check2:
                for j in range(i + 1):
                    ndp[j] += dp[j]

        dp = [x % mod for x in ndp]
        
    ans = 0
    for i in range(n - m, m + 1):
        ans += dp[i]
        ans %= mod

    print(ans)

if __name__ == "__main__":
    main()

