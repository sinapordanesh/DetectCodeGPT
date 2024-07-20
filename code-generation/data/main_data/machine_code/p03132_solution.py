def min_operations(L, A):
    dp = [0] * (L + 1)
    for i in range(1, L+1):
        dp[i] = max(dp[j] + abs(A[i-1] - A[j-1]) for j in range(i))
    return L - max(dp)

# Sample Input 1
print(min_operations(4, [1, 0, 2, 3])) 

# Sample Input 2
print(min_operations(8, [2, 0, 0, 2, 1, 3, 4, 1]))

# Sample Input 3
print(min_operations(7, [314159265, 358979323, 846264338, 327950288, 419716939, 937510582, 0]))