def max_parties(H, W, C, M, NW, NC, NM, heroes, warriors, clerics, mages):
    max_parties = min(H, W + NW, C + NC, M + NM)
    return max_parties

# Sample Input
print(max_parties(2, 1, 1, 1, 1, 1, 1, [[1], [1]], [[1], [1]], [[1], [1]], [[1], [1]]))
print(max_parties(1, 1, 1, 1, 1, 1, 1, [[1], [1]], [[1], [1]], [[0]], [[1]]))
print(max_parties(1, 1, 1, 1, 0, 1, 0, [[1], [1]], [[0]], [[1]], [[0]]))