def min_operations(N, balls):
    operations = 0
    white = []
    black = []
    for i in range(2*N):
        if balls[i][0] == 'W':
            white.append(balls[i][1])
        else:
            black.append(balls[i][1])
    
    white_dict = {}
    black_dict = {}
    
    for i in range(N):
        white_dict[white[i]] = i
        black_dict[black[i]] = i
    
    for i in range(1, N+1):
        operations += abs(white_dict[i] - black_dict[i])
    
    return operations

# Sample Input 1
N = 3
balls = [('B', 1), ('W', 2), ('B', 3), ('W', 1), ('W', 3), ('B', 2)]
print(min_operations(N, balls))

# Sample Input 2
N = 4
balls = [('B', 4), ('W', 4), ('B', 3), ('W', 3), ('B', 2), ('W', 2), ('B', 1), ('W', 1)]
print(min_operations(N, balls))

# Sample Input 3
N = 9
balls = [('W', 3), ('B', 1), ('B', 4), ('W', 1), ('B', 5), ('W', 9), ('W', 2), ('B', 6), ('W', 5), ('B', 3), ('W', 8), ('B', 9), ('W', 7), ('B', 2), ('B', 8), ('W', 4), ('W', 6), ('B', 7)]
print(min_operations(N, balls))