def balls_to_rewrite(N, K, A):
    from collections import Counter
    freq = Counter(A)
    unique_integers = len(freq)
    if unique_integers <= K:
        return 0
    else:
        return sum(sorted(freq.values(), reverse=True)[K:])

# Input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Output
print(balls_to_rewrite(N, K, A))