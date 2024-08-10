def count_partition_divisions(N, A):
    MOD = 10**9 + 7
    prefix_xor = A[:]
    for i in range(1, N):
        prefix_xor[i] ^= prefix_xor[i - 1]
    
    ans = 1
    cnt = {}
    for i in range(N - 1):
        if prefix_xor[i] not in cnt:
            cnt[prefix_xor[i]] = 0
        cnt[prefix_xor[i]] += 1
    
    for key in cnt:
        ans *= (cnt[key] + 1)
        ans %= MOD
        
    return ans

N, *A = map(int, input().split())
print(count_partition_divisions(N, A))