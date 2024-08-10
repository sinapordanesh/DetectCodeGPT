def probability_of_winning(N, K):
    total_probability = 0
    for i in range(1, N+1):
        current_prob = 1 / N
        score = i
        while score < K:
            score *= 2
            current_prob *= 0.5
        total_probability += current_prob
    return total_probability

N, K = map(int, input().split())
print("{:.12f}".format(probability_of_winning(N, K)))