def lexicographically_largest(X, Y, Z):
    if X >= Y and X >= Z:
        return 'a'*X + 'b'*Y + 'c'*Z
    elif Y >= X and Y >= Z:
        return 'b'*Y + 'c'*Z + 'a'*X
    else:
        return 'c'*Z + 'a'*X + 'b'*Y

X, Y, Z = map(int, input().split())
print(lexicographically_largest(X, Y, Z))