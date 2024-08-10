def good_string_length(N, M, S, T):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    if S == T:
        return N

    L = lcm(N, M)
    for i in range(0, L, N):
        if (i + N <= L and S == S[:N] + S[N:]):
            for j in range(0, L, M):
                if (j + M <= L and T == T[:M] + T[M:]):
                    return L

    return -1

# Sample Inputs
print(good_string_length(3, 2, "acp", "ae"))
print(good_string_length(6, 3, "abcdef", "abc"))
print(good_string_length(15, 9, "dnsusrayukuaiia", "dujrunuma"))