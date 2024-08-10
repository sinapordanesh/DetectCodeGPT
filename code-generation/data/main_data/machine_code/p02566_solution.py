def count_distinct_substrings(S):
    n = len(S)
    substrings = set()
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(S[i:j])
    return len(substrings)

S = input().strip()
print(count_distinct_substrings(S))