def sum_of_scores(H, W, K):
    MOD = 10**9 + 7
    total = 0
    
    for i in range(1, H+1):
        for j in range(1, W+1):
            total += (i*j) * (H-i+1) * (W-j+1) % MOD
            
    return total % MOD

# Sample Input 1
print(sum_of_scores(2, 1, 2))

# Sample Input 2
print(sum_of_scores(30, 40, 50))