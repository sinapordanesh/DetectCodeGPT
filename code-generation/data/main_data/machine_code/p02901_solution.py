def minimum_cost_to_unlock(N, M, keys):
    min_cost = float('inf')
    for i in range(1, 2**M):
        cost = 0
        unlocked = set()
        for j in range(M):
            if i & (1 << j):
                cost += keys[j][0]
                for box in keys[j][2:]:
                    unlocked.add(box)
        if len(unlocked) == N:
            min_cost = min(min_cost, cost)
    return min_cost if min_cost != float('inf') else -1

# Sample Input 1
print(minimum_cost_to_unlock(2, 3, [(10, 1, 1), (15, 1, 2), (30, 2, 1, 2)]))

# Sample Input 2
print(minimum_cost_to_unlock(12, 1, [(100000, 1, 2)]))

# Sample Input 3
print(minimum_cost_to_unlock(4, 6, [(67786, 3, 1, 3, 4), (3497, 1, 2), (44908, 3, 2, 3, 4), (2156, 3, 2, 3, 4), (26230, 1, 2), (86918, 1, 3)]))