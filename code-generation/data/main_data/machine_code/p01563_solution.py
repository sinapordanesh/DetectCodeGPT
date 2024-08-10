def connect(R, C, strings):
    dp = [[0] * (1 << C) for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1 << C):
            for k in range(1 << (len(strings[i-1])+1)):
                score = 0
                for l in range(C):
                    if strings[i-1][l] != "_" and (k >> l) & 1:
                        score += sum(strings[i-1][m] == strings[i-1][l] for m in (l-1, l+1))
                dp[i][k] = max(dp[i][k], dp[i-1][j] + score)
    return max(dp[R])

# Sample Input 1
print(connect(2, 4, ["ACM", "ICPC"]))

# Sample Input 2
print(connect(2, 9, ["PROBLEMF", "CONNECT"]))

# Sample Input 3
print(connect(4, 16, ["INTERNATIONAL", "COLLEGIATE", "PROGRAMMING", "CONTEST"]))