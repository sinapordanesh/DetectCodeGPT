def count_friendly_pairs(N, a):
    friendly_pairs = 0
    for i in range(N):
        if i + 1 < a[i] and a[a[i] - 1] == i + 1:
            friendly_pairs += 1
    return friendly_pairs

N = int(input())
a = list(map(int, input().split()))
print(count_friendly_pairs(N, a))