def largest_number_of_different_letters(N, S):
    max_count = 0
    for i in range(1, N):
        X = set(S[:i])
        Y = set(S[i:])
        count = len(X.intersection(Y))
        max_count = max(max_count, count)
    return max_count

N = int(input())
S = input()
print(largest_number_of_different_letters(N, S))