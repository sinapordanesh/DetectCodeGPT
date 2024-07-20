def min_operations(A, B, C):
    total = A + B + C
    max_num = max(A, B, C)
    return (max_num * 3 - total)

# Input
A, B, C = map(int, input().split())

# Output
print(min_operations(A, B, C))