def calculate_penalty(N, P):
    P.sort()
    penalty = 0
    total_time = 0
    
    for i in range(N):
        total_time += P[i]
        penalty += total_time
        
    return penalty

# Sample Input
print(calculate_penalty(3, [10, 20, 30])) # Output: 100
print(calculate_penalty(7, [56, 26, 62, 43, 25, 80, 7])) # Output: 873