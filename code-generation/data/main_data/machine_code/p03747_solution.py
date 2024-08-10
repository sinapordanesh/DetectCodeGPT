def ant_positions(N, L, T, ants):
    positions = []
    
    for i in range(N):
        pos = ants[i][0]
        direction = ants[i][1]
        if direction == 1:
            pos += T
            pos %= L
        else:
            pos -= T
            pos %= L
        positions.append(pos)
    
    return positions

# Sample Input 1
N = 3
L = 8
T = 3
ants = [(0, 1), (3, 2), (6, 1)]
print(*ant_positions(N, L, T, ants))

# Sample Input 2
N = 4
L = 20
T = 9
ants = [(7, 2), (9, 1), (12, 1), (18, 1)]
print(*ant_positions(N, L, T, ants))