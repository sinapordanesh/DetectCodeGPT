def count_triples(N, K):
    count = 0
    for a in range(1, N+1):
        for b in range(1, N+1):
            for c in range(1, N+1):
                if (a+b) % K == 0 and (b+c) % K == 0 and (c+a) % K == 0:
                    count += 1
    return count

N, K = map(int, input().split())
print(count_triples(N, K))