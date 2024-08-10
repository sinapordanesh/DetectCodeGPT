def product_of_arithmetic_progression(Q, queries):
    MOD = 1000003
    ans = []
    
    for x, d, n in queries:
        start = x % MOD
        common_diff = d % MOD
        terms_product = 1
        
        for i in range(n):
            terms_product *= (start + (i * common_diff)) % MOD
            terms_product %= MOD
        
        ans.append(terms_product)
    
    return ans

# Sample Input
Q = 2
queries = [(7, 2, 4), (12345, 67890, 2019)]

print(*product_of_arithmetic_progression(Q, queries), sep="\n")