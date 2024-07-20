def multiplication_table(A, B):
    if A>=1 and A<=9 and B>=1 and B<=9:
        return A*B
    else:
        return -1

A, B = map(int, input().split())
print(multiplication_table(A, B))