def inversion_number(N, K, A):
    MOD = 10**9 + 7
    B = A * K
    
    inv_count = 0
    for i in range(len(B)):
        for j in range(i+1, len(B)):
            if B[i] > B[j]:
                inv_count += 1
    
    return inv_count % MOD

# Sample Input 1
print(inversion_number(2, 2, [2, 1]))

# Sample Input 2
print(inversion_number(3, 5, [1, 1, 1]))

# Sample Input 3
print(inversion_number(10, 998244353, [10, 9, 8, 7, 5, 6, 3, 4, 2, 1]))