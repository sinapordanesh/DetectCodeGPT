def find_pair(X):
    A = int((X + 1) ** (1/5))
    B = -1
    return A, B

X = int(input())
print(*find_pair(X))