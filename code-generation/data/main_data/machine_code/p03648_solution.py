def find_sequence(K):
    N = 2
    while (N - 1) * N // 2 <= K:
        N += 1
    N -= 1
    base = (N - 1) * N // 2
    diff = K - base
    res = [N] * (N - 1 - diff) + [(N - 1) + diff] + [0] + [1] * (N - 2)
    print(N)
    print(*res)