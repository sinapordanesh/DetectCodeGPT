import math

def gcd_of_beauties(N, a):
    MOD = 998244353
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    def beauty(p):
        res = 1
        visited = [False] * N
        for i in range(N):
            if not visited[i]:
                cycle_min = float('inf')
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle_min = min(cycle_min, a[j])
                    cycle_size += 1
                    j = p[j]
                res *= cycle_min
        return res
    
    b_values = [0] * (N+1)
    for i in range(1, N+1):
        total_beauty = 0
        for j in range(1, i+1):
            if i % j == 0:
                total_beauty += beauty([k % i for k in range(j)])
        b_values[i] = total_beauty % MOD
    
    result = b_values[1]
    for i in range(2, N+1):
        result = gcd(result, b_values[i])
    
    return result % MOD

# Sample Input 1
print(gcd_of_beauties(2, [4, 3]))

# Sample Input 2
print(gcd_of_beauties(4, [2, 5, 2, 5]))