def page_number_sum(N, P):
    MOD = 10**9 + 7
    fact = [1]
    for i in range(1, N+1):
        fact.append(fact[-1] * i % MOD)
    
    inv = [1] * (N+1)
    for i in range(2, N+1):
        inv[i] = (-(MOD//i) * inv[MOD%i]) % MOD
    
    ans = 0
    used = [False] * (N+1)
    for i in range(N, 0, -1):
        if P[i-1] == 0:
            cnt = 0
            for j in range(1, P[i-1]):
                if not used[j]:
                    cnt += 1
            
            ans += fact[i-1] * cnt
            ans %= MOD
        else:
            used[P[i-1]] = True
    
    for i in range(1, N+1):
        if not used[i]:
            ans += fact[N]
            ans %= MOD
    
    return ans

# Sample Input 1
print(page_number_sum(4, [0, 2, 3, 0]))

# Sample Input 2
print(page_number_sum(3, [0, 0, 0]))

# Sample Input 3
print(page_number_sum(5, [1, 2, 3, 5, 4]))

# Sample Input 4
print(page_number_sum(1, [0]))

# Sample Input 5
print(page_number_sum(10, [0, 3, 0, 0, 1, 0, 4, 0, 0, 0]))