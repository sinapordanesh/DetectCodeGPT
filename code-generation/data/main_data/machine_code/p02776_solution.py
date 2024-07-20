def deactivate_bombs(N, M, bomb_coords, bomb_states, cord_coords):
    bombs = {}
    for i in range(N):
        bombs[bomb_coords[i]] = bomb_states[i]

    result = []
    for i in range(M):
        start = cord_coords[i][0]
        end = cord_coords[i][1]
        num_activated = sum([bombs[x] for x in range(start, end+1)])

        if num_activated * 2 > end - start + 1:
            result.append(i+1)

    if len(result) == 0:
        print(-1)
    else:
        print(len(result))
        print(*result)