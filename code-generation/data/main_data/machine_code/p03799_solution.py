def max_Scc_groups(N, M):
    return min(N, M // 2, (N + M) // 3)

# Sample Input 1
print(max_Scc_groups(1, 6))

# Sample Input 2
print(max_Scc_groups(12345, 678901))