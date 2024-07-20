def smallest_string(N, K, S):
    T = S[::-1]
    U = S + T
    min_substring = min([U[i:i+N] for i in range(len(U)-N+1)])
    return min_substring

# Sample Input 1
print(smallest_string(5, 1, "bacba"))

# Sample Input 2
print(smallest_string(10, 2, "bbaabbbaab"))