def probability_of_winning(N, A):
    MOD = 10**9 + 7
    
    fact = [1]
    for i in range(1, N+1):
        fact.append((fact[-1] * i) % MOD)
    
    inv_fact = [0] * (N+1)
    inv_fact[N] = pow(fact[N], MOD-2, MOD)
    for i in range(N, 0, -1):
        inv_fact[i-1] = (inv_fact[i] * i) % MOD
    
    def nCr(n, r):
        return (fact[n] * inv_fact[r] * inv_fact[n-r]) % MOD
    
    if A == 1:
        return 2
    
    ans = 0
    for k in range(A, N+1):
        ans = (ans + nCr(N-1, k-1)) % MOD
    
    return (ans * fact[N]) % MOD

# Sample Input
print(probability_of_winning(3, 1))
print(probability_of_winning(3, 2))
print(probability_of_winning(8, 4))
print(probability_of_winning(9999999, 4999))