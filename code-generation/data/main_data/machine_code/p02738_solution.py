def count_permutations(N, M):
    fact = [1]
    for i in range(1, 3*N+1):
        fact.append((fact[-1]*i) % M)
    
    inv_fact = [0] * (3*N+1)
    inv_fact[-1] = pow(fact[-1], M-2, M)
    for i in range(3*N, 0, -1):
        inv_fact[i-1] = (inv_fact[i]*i) % M
    
    def comb(n, r):
        return (fact[n] * inv_fact[r] * inv_fact[n-r]) % M
    
    ans = 0
    for k in range(N+1):
        sign = 1 if k % 2 == 0 else -1
        ans += sign * comb(N, k) * comb(2*N, k) * fact[k]
        ans %= M
    
    return ans

N, M = map(int, input().split())
print(count_permutations(N, M))