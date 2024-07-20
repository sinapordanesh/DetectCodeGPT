def calculate_earnings(X, Y):
    if X == 1 and Y == 1:
        return 1000000
    elif X <= 3 and Y <= 3:
        return 600000
    else:
        return 0

X, Y = map(int, input().split())
print(calculate_earnings(X, Y))