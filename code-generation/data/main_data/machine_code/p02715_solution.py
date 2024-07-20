def gcd_sum(N, K):
    mod = 10**9 + 7
    total = 0
    
    for i in range(1, K+1):
        total += pow(K // i, N, mod)
    
    return total % mod

# Sample Input 1
print(gcd_sum(3, 2))

# Sample Input 2
print(gcd_sum(3, 200))

# Sample Input 3
print(gcd_sum(100000, 100000))