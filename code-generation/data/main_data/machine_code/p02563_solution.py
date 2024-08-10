def calculate_array(N, M, a, b):
    mod = 998244353
    c = [0] * (N + M - 1)
    for i in range(N):
        for j in range(M):
            c[i + j] = (c[i + j] + a[i] * b[j]) % mod
    return c

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = calculate_array(N, M, a, b)
for res in result:
    print(res, end=' ')