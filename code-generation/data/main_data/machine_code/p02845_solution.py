def hat_combinations(N, A):
    MOD = 1000000007
    colors = [0] * N
    for a in A:
        colors[a] += 1
    
    ans = 1
    for c in colors:
        ans = (ans * c) % MOD
    
    return ans

# Input
N = 6
A = [0, 1, 2, 3, 4, 5]
print(hat_combinations(N, A))

N = 3
A = [0, 0, 0]
print(hat_combinations(N, A))

N = 54
A = [0, 0, 1, 0, 1, 2, 1, 2, 3, 2, 3, 3, 4, 4, 5, 4, 6, 5, 7, 8, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 9, 12, 10, 13, 14, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17]
print(hat_combinations(N, A))