def count_consecutive(n, k):
    return n - k + 1

n, k = map(int, input().split())
print(count_consecutive(n, k))