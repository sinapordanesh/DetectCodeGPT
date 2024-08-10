def maximum_fixed_points(N, M, p, pairs):
    p = [int(i) for i in p.split()]
    fixed_points = 0
    for i in range(1, N+1):
        if p[i-1] == i:
            fixed_points += 1
    return fixed_points

# Sample Input
print(maximum_fixed_points(5, 2, "5 3 1 4 2", [(1, 3), (5, 4)]))
print(maximum_fixed_points(3, 2, "3 2 1", [(1, 2), (2, 3)]))
print(maximum_fixed_points(10, 8, "5 3 6 8 7 10 9 1 2 4", [(3, 1), (4, 1), (5, 9), (2, 5), (6, 5), (3, 5), (8, 9), (7, 9)]))
print(maximum_fixed_points(5, 1, "1 2 3 4 5", [(1, 5)]))