def max_operations(N, dots):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (dots[i][0] == dots[j][0] and dots[i][1] == dots[k][1]) or (dots[i][0] == dots[k][0] and dots[i][1] == dots[j][1]) or (dots[j][0] == dots[k][0] and dots[j][1] == dots[i][1]):
                    count += 1
    return count

# Sample Input
print(max_operations(3, [(1, 1), (5, 1), (5, 5)]))
print(max_operations(2, [(10, 10), (20, 20)]))
print(max_operations(9, [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (1, 2), (1, 3), (1, 4), (1, 5)]))