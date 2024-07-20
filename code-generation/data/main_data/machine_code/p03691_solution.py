def turkey_pairs(N, M, actions):
    alive = [1] * N
    pairs = 0
    
    for i in range(M):
        x, y = actions[i]
        if alive[x-1] and alive[y-1]:
            pairs += 1
        alive[x-1] = alive[y-1] = 0

    return pairs

# Sample Input 1
print(turkey_pairs(3, 1, [(1, 2)]))

# Sample Input 2
print(turkey_pairs(4, 3, [(1, 2), (3, 4), (2, 3)]))

# Sample Input 3
print(turkey_pairs(3, 2, [(1, 2), (1, 2)]))

# Sample Input 4
print(turkey_pairs(10, 10, [(8, 9), (2, 8), (4, 6), (4, 9), (7, 8), (2, 8), (1, 8), (3, 4), (3, 4), (2, 7)]))