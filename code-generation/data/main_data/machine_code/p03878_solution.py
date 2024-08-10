def minimize_cable_length(N, a, b):
    MOD = 10**9 + 7
    a.sort()
    b.sort()
    ans = 1
    for i in range(N):
        ans *= abs(a[i] - b[i])
        ans %= MOD
    return ans

# Sample Input
N = 3
a = [3, 10, 8]
b = [7, 5, 12]
print(minimize_cable_length(N, a, b))