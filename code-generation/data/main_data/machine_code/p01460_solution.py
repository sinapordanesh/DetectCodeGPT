def matrix_operation(N, Q, A, B, C, D, E, F, G, operations):
    matrix = [[0] * N for _ in range(N)]
    for r in range(1, N+1):
        for c in range(1, N+1):
            matrix[r-1][c-1] = (r * A + c * B) % C
    
    for operation in operations:
        if operation[0] == 'WR':
            r, c, v = operation[1:]
            matrix[r-1][c-1] = v
        elif operation[0] == 'CP':
            r1, c1, r2, c2 = operation[1:]
            matrix[r2-1][c2-1] = matrix[r1-1][c1-1]
        elif operation[0] == 'SR':
            r1, r2 = operation[1:]
            matrix[r1-1], matrix[r2-1] = matrix[r2-1], matrix[r1-1]
        elif operation[0] == 'SC':
            c1, c2 = operation[1:]
            for i in range(N):
                matrix[i][c1-1], matrix[i][c2-1] = matrix[i][c2-1], matrix[i][c1-1]
        elif operation[0] == 'RL':
            matrix = list(zip(*matrix[::-1]))
        elif operation[0] == 'RR':
            matrix = list(zip(*matrix[::-1]))[::-1]
        elif operation[0] == 'RH':
            matrix = matrix[::-1]
        elif operation[0] == 'RV':
            matrix = [row[::-1] for row in matrix]
    
    h = 314159265
    for r in range(D, E+1):
        for c in range(F, G+1):
            h = (31 * h + matrix[r-1][c-1]) % 1000000007
    
    return h