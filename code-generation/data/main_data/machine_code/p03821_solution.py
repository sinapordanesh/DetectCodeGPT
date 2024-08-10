def min_presses(N, values):
    result = 0
    remainder = 0
    for i in range(N-1, -1, -1):
        total = values[i][0] + remainder
        if total % values[i][1] != 0:
            remainder += values[i][1] - (total % values[i][1])
            result += remainder
    return result

# Sample Input 1
N = 3
values = [(3, 5), (2, 7), (9, 4)]
print(min_presses(N, values))

# Sample Input 2
N = 7
values = [(3, 1), (4, 1), (5, 9), (2, 6), (5, 3), (5, 8), (9, 7)]
print(min_presses(N, values))