def number_of_strings(S):
    MOD = 998244353
    n = len(S)
    count = 1
    for i in range(n-1):
        if S[i] != S[i+1]:
            count = (count * 3) % MOD
    return count

S = input().strip()
print(number_of_strings(S))