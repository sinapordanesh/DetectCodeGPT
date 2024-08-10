def f(X):
    left, right = 2, 2
    for i in range(X-1):
        left, right = right, 2*right + left
    return right

X = int(input())
print(f(X))