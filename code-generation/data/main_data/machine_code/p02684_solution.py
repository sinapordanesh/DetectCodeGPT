def teleporter_town(N, K, A):
    current_town = 1
    visited = set()
    cycle_start = None
    
    for _ in range(K):
        if current_town in visited:
            cycle_start = current_town
            break
        visited.add(current_town)
        current_town = A[current_town-1]

    if cycle_start is not None:
        cycle_length = len(visited) - visited.index(cycle_start)
        remaining_steps = (K - visited.index(cycle_start)) % cycle_length
        for _ in range(remaining_steps):
            current_town = A[current_town-1]
    
    return current_town

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(teleporter_town(N, K, A))