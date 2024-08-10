def exhibition_place(N, lines):
    x_total = 0
    y_total = 0
    
    for i in range(N):
        x_total += lines[i][2] / lines[i][0]
        y_total += lines[i][2] / lines[i][1]
    
    x_coordinate = x_total / N
    y_coordinate = y_total / N
    
    return x_coordinate, y_coordinate

# Sample Input 1
N = 3
lines = [[1, 1, 1], [2, -1, 2], [-1, 2, 2]]
print(exhibition_place(N, lines))

# Sample Input 2
N = 4
lines = [[1, 1, 2], [1, -1, 0], [3, -1, -2], [1, -3, 4]]
print(exhibition_place(N, lines))

# Sample Input 3
N = 7
lines = [[1, 7, 8], [-2, 4, 9], [3, -8, -5], [9, 2, -14], [6, 7, 5], [-8, -9, 3], [3, 8, 10]]
print(exhibition_place(N, lines))