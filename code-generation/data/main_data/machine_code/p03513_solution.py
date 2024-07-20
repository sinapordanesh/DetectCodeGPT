def island_probability(N, M, islands):
    total_scenarios = 2 ** M
    count = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            reachable_i = set()
            reachable_j = set()
            for k in range(M):
                if islands[k][0] == i:
                    reachable_i.add(islands[k][1])
                if islands[k][1] == i:
                    reachable_i.add(islands[k][0])
                if islands[k][0] == j:
                    reachable_j.add(islands[k][1])
                if islands[k][1] == j:
                    reachable_j.add(islands[k][0])
            if len(reachable_i.intersection(reachable_j)) > 0:
                count += 1
    return (count * pow(2, M, 10**9 + 7)) % (10**9 + 7)

# Sample Input 1
print(island_probability(4, 3, [(1, 3), (2, 3), (3, 4)]))

# Sample Input 2
print(island_probability(5, 5, [(1, 3), (2, 4), (3, 4), (3, 5), (4, 5)]))

# Sample Input 3
print(island_probability(6, 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 6)]))