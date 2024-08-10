def solve_sequence(N, K, A):
    gcd = A[0]
    for i in range(1, N):
        gcd = math.gcd(gcd, A[i])
    return gcd

# Sample Input 1
print(solve_sequence(2, 3, [8, 20]))

# Sample Input 2
print(solve_sequence(2, 10, [3, 5]))

# Sample Input 3
print(solve_sequence(4, 5, [10, 1, 2, 22]))

# Sample Input 4
print(solve_sequence(8, 7, [1, 7, 5, 6, 8, 2, 6, 5]))