def min_changes(S, T):
    min_changes = len(T)
    for i in range(len(S) - len(T) + 1):
        changes = sum([1 for j in range(len(T)) if S[i+j] != T[j]])
        min_changes = min(min_changes, changes)
    return min_changes

# Test cases
print(min_changes("cabacc", "abc"))
print(min_changes("codeforces", "atcoder"))