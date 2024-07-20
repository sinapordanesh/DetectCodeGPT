def crackers_distribution(N, K):
    return N % K if N >= K else 0

N, K = map(int, input().split())
print(crackers_distribution(N, K))