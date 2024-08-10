def minimum_santa(N, M, L, roads, requests):
    min_santa = 0
    for i in range(1, max(requests.values()) + 1):
        count = sum(1 for p, t in requests.items() if t == i)
        min_santa = max(min_santa, count)
    return min_santa

# Sample Input
N = 3
M = 2
L = 3
roads = [(0, 1, 10), (1, 2, 10)]
requests = {1: 10, 2: 0}
print(minimum_santa(N, M, L, roads, requests))

N = 3
M = 2
L = 4
roads = [(0, 1, 10), (1, 2, 10)]
requests = {1: 10, 2: 20, 0: 40}
print(minimum_santa(N, M, L, roads, requests))

N = 10
M = 10
L = 10
roads = [(0, 1, 39), (2, 3, 48), (3, 5, 20), (4, 8, 43), (3, 9, 10), (8, 9, 40), (3, 4, 5), (5, 7, 20), (1, 7, 93), (1, 3, 20)]
requests = {1: 100000000, 2: 100, 3: 543, 4: 500, 5: 400, 6: 300, 7: 200, 8: 100, 9: 100}
print(minimum_santa(N, M, L, roads, requests))