def min_roads(N, P):
    MOD = 10**9 + 7
    count = 0
    for p in P:
        if p == -1:
            count += 1
    
    result = pow(N-1, count, MOD)
    
    return result

# Sample Input 1
print(min_roads(4, [2, 1, -1, 3])) # Output 8

# Sample Input 2
print(min_roads(2, [2, 1])) # Output 1

# Sample Input 3
print(min_roads(10, [2, 6, 9, -1, 6, 9, -1, -1, -1, -1])) # Output 527841