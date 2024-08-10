def min_difference(S):
    min_diff = float('inf')
    for i in range(len(S) - 2):
        X = int(S[i:i+3])
        min_diff = min(min_diff, abs(X - 753))
    return min_diff

S = input().strip()
print(min_difference(S))