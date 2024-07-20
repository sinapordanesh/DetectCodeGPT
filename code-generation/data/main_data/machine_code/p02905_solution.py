def lcm(a, b):
    return a * b // math.gcd(a, b)

def sum_lcm(N, A):
    MOD = 998244353
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += lcm(A[i], A[j])
            ans %= MOD
    return ans % MOD

# Sample Input 1
print(sum_lcm(3, [2, 4, 6]))

# Sample Input 2
print(sum_lcm(8, [1, 2, 3, 4, 6, 8, 12, 12]))

# Sample Input 3
print(sum_lcm(10, [356822, 296174, 484500, 710640, 518322, 888250, 259161, 609120, 592348, 713644]))