def make_pairs(N, compatibility):
    MOD = 10**9 + 7
    
    def solve(mask, woman):
        if mask == (1 << N) - 1:
            return 1
        if woman == N:
            return 0
        
        result = 0
        for man in range(N):
            if (mask >> man) & 1 == 0 and compatibility[man][woman]:
                result += solve(mask | (1 << man), woman + 1)
                result %= MOD
        
        return result
    
    return solve(0, 0) % MOD