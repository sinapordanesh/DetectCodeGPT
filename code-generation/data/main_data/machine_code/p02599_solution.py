def count_colors(N, Q, colors, queries):
    result = []
    for query in queries:
        l, r = query
        result.append(len(set(colors[l-1:r])))
    return result

# Sample Input 1
N = 4
Q = 3
colors = [1, 2, 1, 3]
queries = [(1, 3), (2, 4), (3, 3)]
print(*count_colors(N, Q, colors, queries))

# Sample Input 2
N = 10
Q = 10
colors = [2, 5, 6, 5, 2, 1, 7, 9, 7, 2]
queries = [(5, 5), (2, 4), (6, 7), (2, 2), (7, 8), (7, 9), (1, 8), (6, 9), (8, 10), (6, 8)]
print(*count_colors(N, Q, colors, queries))