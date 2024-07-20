def sum_of_pairs(N, A):
    MOD = 10**9 + 7
    result = 0
    
    for i in range(N-1):
        for j in range(i+1, N):
            result += A[i] * A[j]
    
    return result % MOD

# Sample Input
N = 3
A = [1, 2, 3]
print(sum_of_pairs(N, A))

N = 4
A = [141421356, 17320508, 22360679, 244949]
print(sum_of_pairs(N, A))