def possible_to_reach_state(N, K, A):
    if K in A or max(A) >= K:
        return "POSSIBLE"
    total = sum(A)
    if total < K or (total-K) % 2 == 1:
        return "IMPOSSIBLE"
    return "POSSIBLE"