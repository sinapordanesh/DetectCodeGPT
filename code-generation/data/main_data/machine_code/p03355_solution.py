def kth_smallest_substring(s, K):
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.add(s[i:j])
    sorted_substrings = sorted(list(substrings))
    return sorted_substrings[K-1]