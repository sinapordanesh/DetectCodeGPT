def icpc_teams(N, M, relationships):
    MOD = 10**9 + 9
    
    def dfs(i, mask, bad_mask):
        if i == N * 3:
            return 1
        
        if i % 3 == 0:
            return dfs(i + 1, mask, bad_mask)
        
        res = 0
        if (mask >> i) & 1 == 0 and (bad_mask >> i) & 1 == 0:
            res = (res + dfs(i + 1, mask | (1 << i), bad_mask)) % MOD
        
        res = (res + dfs(i + 1, mask, bad_mask | (1 << i))) % MOD
        
        return res
    
    relations = 0
    for A, B, C in relationships:
        if C == 0:
            relations |= 1 << (3 * (A - 1) + (B - 1) % 3)
        else:
            relations |= 1 << (3 * (A - 1) + ((B - 1) % 3) + 9)
    
    return dfs(0, 0, relations)

# Sample Input
N = 2
M = 2
relationships = [(1, 2, 0), (3, 4, 1)]

print(icpc_teams(N, M, relationships))