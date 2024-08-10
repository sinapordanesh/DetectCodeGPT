def min_operations_to_palindrome(S):
    def is_palindrome(s):
        return s == s[::-1]
    
    if not S:
        return 0
    
    if not is_palindrome(S):
        return -1
    
    n = len(S)
    res = 0
    for i in range(n//2):
        if S[i] != S[n-1-i]:
            res += 1
    return res

# Sample Input 1
print(min_operations_to_palindrome("eel"))

# Sample Input 2
print(min_operations_to_palindrome("ataatmma"))

# Sample Input 3
print(min_operations_to_palindrome("snuke"))