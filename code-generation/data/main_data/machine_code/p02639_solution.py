def find_zero_variable(x1, x2, x3, x4, x5):
    if x1 == 0:
        return 1
    elif x2 == 0:
        return 2
    elif x3 == 0:
        return 3
    elif x4 == 0:
        return 4
    elif x5 == 0:
        return 5

x1, x2, x3, x4, x5 = map(int, input().split())
print(find_zero_variable(x1, x2, x3, x4, x5))