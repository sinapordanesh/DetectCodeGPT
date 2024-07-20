def maximum_happiness(N, M, A):
    A.sort(reverse=True)
    total_happiness = sum(A)
    
    num_handshakes = min(M, N-1)
    remaining_handshakes = M - num_handshakes
    
    max_happiness = 0
    for i in range(num_handshakes):
        max_happiness += A[i] + A[i]
    
    max_happiness += remaining_handshakes * min(A[0], A[1])
    
    return max_happiness

# Sample Input 1
print(maximum_happiness(5, 3, [10, 14, 19, 34, 33]))

# Sample Input 2
print(maximum_happiness(9, 14, [1, 3, 5, 110, 24, 21, 34, 5, 3]))

# Sample Input 3
print(maximum_happiness(9, 73, [67597, 52981, 5828, 66249, 75177, 64141, 40773, 79105, 16076]))