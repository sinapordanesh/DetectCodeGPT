def num_occurences(s, l, r):
    s = s * (10**100)
    substring = s[l-1:r]
    occurrences = [0]*26
    for char in substring:
        if 'a' <= char <= 'z':
            occurrences[ord(char) - ord('a')] += 1
    return occurrences

# Test the function
print(*num_occurences("abaaba", 6, 10))
print(*num_occurences("xx", 1, 1000000000000000000))
print(*num_occurences("vgxgpuamkvgxgvgxgpuamkvgxg", 1, 1000000000000000000))