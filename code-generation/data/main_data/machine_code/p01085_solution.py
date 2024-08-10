def successful_applicants(m, n_min, n_max, scores):
    max_gap = 0
    num_successful = n_min
    for n in range(n_min, n_max+1):
        gap = scores[n-1] - scores[n]
        if gap > max_gap:
            max_gap = gap
            num_successful = n
    return num_successful

# Read input
while True:
    m, n_min, n_max = map(int, input().split())
    if m == 0 and n_min == 0 and n_max == 0:
        break
    scores = [int(input()) for _ in range(m)]
    print(successful_applicants(m, n_min, n_max, scores))