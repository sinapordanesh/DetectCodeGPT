def sum_f(N, K, A):
    MOD = 10**9 + 7
    A.sort()
    ans = 0
    for i in range(K-1, N):
        ans += A[i] * (i*(i+1)//2 - (N-i-1)*(N-i)//2)
    return ans % MOD

# Sample Input 1
print(sum_f(4, 2, [1, 1, 3, 4])) 

# Sample Input 2
print(sum_f(6, 3, [10, 10, 10, -10, -10, -10]))

# Sample Input 3
print(sum_f(3, 1, [1, 1, 1]))

# Sample Input 4
print(sum_f(10, 6, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 0, 0, 0, 0, 0]))