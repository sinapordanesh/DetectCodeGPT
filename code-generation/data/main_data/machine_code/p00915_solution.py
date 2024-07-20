def last_ant_leave_tunnel(n, l, ants):
    positions = [0] * n
    directions = [0] * n
    for i in range(n):
        direction, position = ants[i]
        positions[i] = position
        directions[i] = direction
    
    time = 0
    while any(0 <= p < l for p in positions):
        time += 1
        for i in range(n):
            if 0 <= positions[i] < l:
                positions[i] += 1 if directions[i] == 'R' else -1
                for j in range(n):
                    if i != j and positions[i] == positions[j]:
                        directions[i] = 'R' if directions[i] == 'L' else 'L'
                        directions[j] = 'R' if directions[j] == 'L' else 'L'
    
    return time, directions.index(directions[-1]) + 1