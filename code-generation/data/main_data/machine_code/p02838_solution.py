def xor_sum(N, A):
    MOD = 10**9 + 7
    total_xor_sum = 0
    
    for i in range(N-1):
        for j in range(i+1, N):
            total_xor_sum += A[i] ^ A[j]
    
    return total_xor_sum % MOD

# Sample Input 1
print(xor_sum(3, [1, 2, 3]))

# Sample Input 2
print(xor_sum(10, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))

# Sample Input 3
print(xor_sum(10, [3, 14, 159, 2653, 58979, 323846, 2643383, 27950288, 419716939, 9375105820]))