def max_coins(A, B):
    return max(A + A-1, B + B-1, A + B)

A, B = map(int, input().split())
print(max_coins(A, B))