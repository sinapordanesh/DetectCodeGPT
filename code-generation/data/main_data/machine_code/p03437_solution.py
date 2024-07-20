def find_multiple_not_divisible_by_y(X, Y):
    for i in range(1, int(10**18)+1):
        if i%X == 0 and i%Y != 0:
            return i
    return -1

X, Y = map(int, input().split())
result = find_multiple_not_divisible_by_y(X, Y)
print(result)