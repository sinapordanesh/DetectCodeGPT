def count_pairs(S):
    MOD = 10**9 + 7
    ans = 0
    for i in range(1, S+1):
        sum_digits = len(str(i))
        remaining_sum = S - sum_digits
        if remaining_sum >= 0:
            ans += pow(10, remaining_sum, MOD)
    return ans % MOD

S = int(input())
print(count_pairs(S))