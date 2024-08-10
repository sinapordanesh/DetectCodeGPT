def expected_number_of_games(N, A, B, C):
    mod = 10**9 + 7
    P = 0
    Q = 0
    
    for k in range(1, N+1):
        P += k * pow(C, k-1, mod) * (pow(A, N-k, mod) + pow(B, N-k, mod)) % mod
        Q += pow(C, k-1, mod) % mod
    
    R = (P * pow(Q, -1, mod)) % mod
    return R

# Sample Input 1
print(expected_number_of_games(1, 25, 25, 50))

# Sample Input 2
print(expected_number_of_games(4, 50, 50, 0))

# Sample Input 3
print(expected_number_of_games(1, 100, 0, 0))

# Sample Input 4
print(expected_number_of_games(100000, 31, 41, 28))