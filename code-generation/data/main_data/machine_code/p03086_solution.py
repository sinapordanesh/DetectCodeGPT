def longest_ACGT_substring(S):
    max_len = 0
    current_len = 0
    
    for char in S:
        if char in {'A', 'C', 'G', 'T'}:
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
            
    return max_len

# Test the function with the sample inputs
print(longest_ACGT_substring("ATCODER"))
print(longest_ACGT_substring("HATAGAYA"))
print(longest_ACGT_substring("SHINJUKU"))