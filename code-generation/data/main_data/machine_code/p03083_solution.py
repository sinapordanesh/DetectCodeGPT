def eat_chocolates(B, W):
    MOD = 10**9 + 7
    inv2 = pow(2, MOD-2, MOD)
    ans = []
    s1, s2 = 1, 1
    for i in range(1, B+W+1):
        s1 = s1 * (B+W-i+1) % MOD
        s2 = s2 * i % MOD
        if i < B:
            p = 0
        else:
            p = (s1 * pow(s2 * pow(B, MOD-2, MOD) % MOD, MOD-2, MOD) + MOD) % MOD
        ans.append(p)
    return ans

# Sample Input 1
B1 = 2
W1 = 1
print(*eat_chocolates(B1, W1))

# Sample Input 2
B2 = 3
W2 = 2
print(*eat_chocolates(B2, W2))

# Sample Input 3
B3 = 6
W3 = 9
print(*eat_chocolates(B3, W3))