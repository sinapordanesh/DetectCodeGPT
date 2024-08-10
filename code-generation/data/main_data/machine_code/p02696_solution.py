def max_value(A, B, N):
    max_val = 0
    for x in range(N+1):
        val = (A*x // B) - (A * (x // B))
        if val > max_val:
            max_val = val
    return max_val

# Sample Input 1
print(max_value(5, 7, 4))

# Sample Input 2
print(max_value(11, 10, 9))