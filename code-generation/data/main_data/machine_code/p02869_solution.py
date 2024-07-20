def partition_integers(N, K):
    if N % 2 == 1:
        return f"{K} {K + 2} {K + 4}"
    else:
        return -1

N, K = map(int, input().split())
result = partition_integers(N, K)
print(result)