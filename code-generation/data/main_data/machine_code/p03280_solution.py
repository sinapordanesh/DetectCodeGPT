def calculate_area(A, B):
    return (A-1)*(B-1) - 1

A, B = map(int, input().split())
print(calculate_area(A, B))