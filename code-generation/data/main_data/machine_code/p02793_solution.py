def min_possible_value(N, A):
    from math import gcd
    MOD = 10**9 + 7
    
    lcm = A[0]
    for i in range(1, N):
        lcm = (lcm * A[i]) // gcd(lcm, A[i])
    
    result = 0
    for i in range(N):
        result += (lcm // A[i])
        
    return result % MOD

# Sample Input 1
print(min_possible_value(3, [2, 3, 4]))

# Sample Input 2
print(min_possible_value(5, [12, 12, 12, 12, 12]))

# Sample Input 3
print(min_possible_value(3, [1000000, 999999, 999998]))