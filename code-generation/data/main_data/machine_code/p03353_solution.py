def kth_smallest_substring(s, K):
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.add(s[i:j])
    
    substrings = sorted(substrings)
    
    return substrings[K-1]