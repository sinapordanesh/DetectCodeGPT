def is_strong_palindrome(S):
    def is_palindrome(s):
        return s == s[::-1]
    
    N = len(S)
    
    if not is_palindrome(S):
        return "No"
    
    if not is_palindrome(S[:int((N-1)/2)]):
        return "No"
    
    if not is_palindrome(S[int((N+3)/2)-1:]):
        return "No"
    
    return "Yes"