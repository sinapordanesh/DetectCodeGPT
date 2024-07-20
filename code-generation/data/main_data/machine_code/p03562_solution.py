def count_integers(N, X, A):
    MOD = 998244353
    count = 0
    
    xor_values = set()
    
    for a in A:
        xor_values.add(int(a, 2))
    
    xor_values.add(X)
    
    for i in range(len(bin(X))-2):
        if (X >> i) & 1 == 1:
            count += pow(2, max(0, N-2-i), MOD)
            count %= MOD
    
    for a in xor_values:
        for b in xor_values:
            xor_val = a ^ b
            if xor_val <= X:
                count += 1
                count %= MOD
    
    return count

# Input
N, X = map(int, input().split())
A = [input() for _ in range(N)]

# Output
print(count_integers(N, X, A))