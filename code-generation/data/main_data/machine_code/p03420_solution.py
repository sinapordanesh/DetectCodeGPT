def possible_pairs(N, K):
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a % b >= K:
                count += 1
    return count

N, K = map(int, input().split())
print(possible_pairs(N, K))