def min_cost(N, towns):
    towns.sort()
    min_cost = 0
    for i in range(1, N):
        min_cost += min(abs(towns[i][0] - towns[i-1][0]), abs(towns[i][1] - towns[i-1][1]))
    return min_cost

# Sample Input
N = 3
towns = [(1, 5), (3, 9), (7, 8)]
print(min_cost(N, towns))

N = 6
towns = [(8, 3), (4, 9), (12, 19), (18, 1), (13, 5), (7, 6)]
print(min_cost(N, towns))