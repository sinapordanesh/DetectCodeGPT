def dance_positions(N, T):
    positions = [i for i in range(3**N)]
    
    for song in T:
        new_positions = []
        if song == 'S':
            for i in range(3**N):
                j = int(str(i), 3).replace('1', 'x').replace('2', '1').replace('x', '2')
                new_positions.append(j % (3**N))
        else:
            for i in range(3**N):
                new_positions.append((i + 1) % (3**N))
        
        positions = [new_positions[p] for p in positions]
    
    return positions

N = int(input())
T = input().strip()
result = dance_positions(N, T)
print(*result)