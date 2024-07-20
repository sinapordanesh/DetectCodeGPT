def find_longest_subsequence(N, K, *X):
    S = set(X)

    def is_subsequence(s1, s2):
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)

    longest_subsequence = ""
    for i in range(1, 2**N):
        for j in range(i+1, 2**N+1):
            subsequence = X[0][i:j]
            count = sum(1 for s in S if is_subsequence(subsequence, s))
            if count >= K and (len(subsequence) > len(longest_subsequence) or (len(subsequence) == len(longest_subsequence) and subsequence < longest_subsequence)):
                longest_subsequence = subsequence

    return longest_subsequence

# Sample Input 1
print(find_longest_subsequence(3, 4, "1", "01", "1011", "01001110"))

# Sample Input 2
print(find_longest_subsequence(4, 6, "1", "01", "1011", "10111010", "1101110011111101"))

# Sample Input 3
print(find_longest_subsequence(2, 5, "0", "11", "1111"))