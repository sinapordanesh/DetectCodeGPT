def num_squares_crossed(A, B, C, D):
    x = abs(C - A)
    y = abs(D - B)
    return math.gcd(x, y) - 1 + 1

A, B, C, D = map(int, input().split())
print(num_squares_crossed(A, B, C, D))