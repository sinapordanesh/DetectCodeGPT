def possible_orders(N, A):
    MOD = 10**9 + 7
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    if any(cnt[i] > 2 for i in range(1, N)):
        return 0
    if cnt[0] > 1:
        return 0
    if cnt[N] > 1:
        return 0
    if cnt[0] + cnt[N] > 1 and cnt[1] != cnt[N - 1]:
        return 0
    ans = 1
    for i in range(1, N + 1):
        if cnt[i] == 0:
            ans = ans * cnt[i - 1] % MOD
        if cnt[i] == 1:
            if cnt[i - 1] == 0:
                return 0
    return ans

# Sample Input
print(possible_orders(5, [2, 4, 4, 0, 2]))
print(possible_orders(7, [6, 4, 0, 2, 4, 0, 2]))
print(possible_orders(8, [7, 5, 1, 1, 7, 3, 5, 3]))