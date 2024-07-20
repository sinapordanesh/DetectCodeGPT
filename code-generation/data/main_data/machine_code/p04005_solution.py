def min_difference(A, B, C):
    total_blocks = A * B * C
    if total_blocks % 2 == 0:
        return 0
    elif A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        return 0
    else:
        return 1

A, B, C = map(int, input().split())
print(min_difference(A, B, C))