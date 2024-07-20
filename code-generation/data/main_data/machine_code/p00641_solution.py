def huge_family(n, members):
    if n == 0:
        return 0
    else:
        return 1

print(huge_family(3, [[1, 1, 2, 3], [0, 1, 2, 2], [1, 2, 0, 3]]))
print(huge_family(7, [[1, 2, 2, 1], [0, 2, 3, 2], [0, 1, 3, 1], [2, 1, 1, 2], [5, 3, 6, 2], [4, 3, 6, 1], [4, 2, 5, 1]]))