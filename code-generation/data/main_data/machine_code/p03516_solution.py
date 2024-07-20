def find_number_of_graphs(N, d):
    MOD = 10**9 + 7
    fact = [1]
    for i in range(1, N):
        fact.append((fact[-1] * i) % MOD)
    
    ans = fact[N-2]
    for i in d:
        ans = (ans * pow(fact[i-1], MOD-2, MOD)) % MOD
    
    return ans

N = int(input())
d = list(map(int, input().split()))
print(find_number_of_graphs(N, d))