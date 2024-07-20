def min_operations(x):
    if x % 11 == 0:
        return x // 11 * 2
    elif x % 11 <= 6:
        return x // 11 * 2 + 1
    else:
        return x // 11 * 2 + 2

x = int(input())
print(min_operations(x))