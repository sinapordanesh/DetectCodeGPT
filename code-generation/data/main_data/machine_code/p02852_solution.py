def find_winning_sequence(N, M, S):
    if S[0] == '1' or S[N] == '1':
        print(-1)
        return
    
    dp = [-1] * (N + 1)
    dp[0] = 0
    
    for i in range(N):
        if dp[i] == -1:
            continue
        
        for j in range(1, M + 1):
            if i + j > N:
                continue
            if S[i + j] == '1':
                continue
            if dp[i + j] == -1 or dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1
    
    if dp[N] == -1:
        print(-1)
        return
    
    result = []
    i = N
    while i > 0:
        for j in range(1, M + 1):
            if i - j >= 0 and dp[i - j] == dp[i] - 1:
                result.append(j)
                i -= j
                break
    
    print(*result[::-1])

n, m, s = map(int, input().split())
find_winning_sequence(n, m, input())