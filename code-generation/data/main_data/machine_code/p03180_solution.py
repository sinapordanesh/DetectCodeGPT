def max_total_score(N, a):
    max_score = 0
    for i in range(2 ** N):
        group = []
        for j in range(N):
            if (i >> j) & 1:
                group.append(j)
        score = 0
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                score += a[group[i]][group[j]]
        max_score = max(max_score, score)
    return max_score

# Input
N = 3
a = [
    [0, 10, 20],
    [10, 0, -100],
    [20, -100, 0]
]

# Output
print(max_total_score(N, a))