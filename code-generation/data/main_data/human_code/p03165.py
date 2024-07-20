def main():

    s = str(input())
    t = str(input())

    dp = [[0]*3100 for _ in range(3100)]

    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])

    i = len(s)
    j = len(t)
    ans = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans.append(s[i-1])
            i -= 1
            j -= 1
    ans.reverse()
    print(''.join(ans))

if __name__ == '__main__':
    main()
