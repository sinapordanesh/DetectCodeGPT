MOD = 10**9 + 7

def count_ways_to_white(N, S):
    ans = 1
    for i in range(N):
        if S[i] == S[i + N]:
            ans = ans * 2 % MOD
        else:
            ans = ans * 1 % MOD
    return ans

N, S = map(int, input().split())
print(count_ways_to_white(N, S))