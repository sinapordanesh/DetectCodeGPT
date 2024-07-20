def max_allowance(A, B, C):
    return max(A+B+C, A+B*C, A*B+C, A*B*C)

A, B, C = map(int, input().split())
print(max_allowance(A, B, C))