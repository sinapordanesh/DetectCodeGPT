def expected_inversion(N, K, p):
    MOD = 998244353
    inv = 0
    for i in range(N-K+1):
        for j in range(i, i+K):
            for l in range(j+1, i+K):
                if p[j] > p[l]:
                    inv += 1
    result = (inv * pow(N-K+1, MOD-2, MOD)) % MOD
    print(result)

# Sample Input 1
N = 3
K = 2
p = [1, 2, 3]
expected_inversion(N, K, p)

# Sample Input 2
N = 10
K = 3
p = [1, 8, 4, 9, 2, 3, 7, 10, 5, 6]
expected_inversion(N, K, p)