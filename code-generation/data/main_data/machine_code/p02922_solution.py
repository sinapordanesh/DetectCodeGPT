def min_power_strips(A, B):
    return (B + A - 1) // A

A, B = map(int, input().split())
print(min_power_strips(A, B))