def possible_orders(N, A):
    MOD = 10**9 + 7
    
    count = [0] * (N+1)
    for a in A:
        if a >= N:
            return 0
        count[a] += 1
    
    if count[0] != 1:
        return 0
        
    ans = 1
    for i in range(1, N):
        ans *= count[i-1] ** count[i] % MOD
        ans %= MOD
    
    return ans

# Sample Input 1
print(possible_orders(5, [2, 4, 4, 0, 2]))

# Sample Input 2
print(possible_orders(7, [6, 4, 0, 2, 4, 0, 2]))

# Sample Input 3
print(possible_orders(8, [7, 5, 1, 1, 7, 3, 5, 3]))