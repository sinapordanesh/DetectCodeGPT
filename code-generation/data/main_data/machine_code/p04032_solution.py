def unbalanced_substring(s):
    n = len(s)
    for i in range(n-1):
        count = 1
        j = i + 1
        while j < n and s[j] == s[i]:
            count += 1
            j += 1
        if count > n / 2:
            return i+1, j
    return -1, -1