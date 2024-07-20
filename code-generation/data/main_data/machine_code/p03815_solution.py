def min_operations(x):
    if x % 11 == 0:
        print(x // 11 * 2)
    else:
        print(x // 11 * 2 + 1)