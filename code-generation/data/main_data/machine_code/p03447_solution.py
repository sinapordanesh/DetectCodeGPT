def remaining_amount(X, A, B):
    return X - A - ((X - A) // B) * B

X, A, B = map(int, input().split())
print(remaining_amount(X, A, B))