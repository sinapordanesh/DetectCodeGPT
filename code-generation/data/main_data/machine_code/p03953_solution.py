def rabbit_position(N, x, M, K, jumps):
    def jump_position(start, end, x):
        return end + end - start - x
    
    positions = x.copy()
    for _ in range(K):
        new_positions = [0]*N
        for j in range(M):
            for i in range(1, N-1):
                new_positions[i] += 0.5*(positions[jumps[j][i-1]] + positions[jumps[j][i+1]])
        positions = new_positions.copy()
    
    return positions

N = 3
x = [-1, 0, 2]
M = 1
K = 1
jumps = [[1, 1]]

output = rabbit_position(N, x, M, K, jumps)
for pos in output:
    print(pos)