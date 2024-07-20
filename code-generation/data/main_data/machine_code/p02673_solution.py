def expected_gain_optimal_strategy(N, A, B):
    A = [0] + A
    B = [0] + B
    
    dp = [0] * (N+1)
    
    for i in range(1, N+1):
        dp[i] = A[i]
    
    for i in range(1, N+1):
        dp[i] = max(dp[i], (dp[i-1] + dp[i+1] - B[i]) / 2)
    
    return dp[N]

N = 5
A = [4, 2, 6, 3, 5]
B = [1, 1, 1, 1, 1]
print('%.12f' % expected_gain_optimal_strategy(N, A, B))

N = 4
A = [100, 0, 100, 0]
B = [0, 100, 0, 100]
print('%.12f' % expected_gain_optimal_strategy(N, A, B))

N = 14
A = [4839, 5400, 6231, 5800, 6001, 5200, 6350, 7133, 7986, 8012, 7537, 7013, 6477, 5912]
B = [34, 54, 61, 32, 52, 61, 21, 43, 65, 12, 45, 21, 1, 4]
print('%.12f' % expected_gain_optimal_strategy(N, A, B))

N = 10
A = [470606482521, 533212137322, 116718867454, 746976621474, 457112271419, 815899162072, 641324977314, 88281100571, 9231169966, 455007126951]
B = [26, 83, 30, 59, 100, 88, 84, 91, 54, 61]
print('%.12f' % expected_gain_optimal_strategy(N, A, B))