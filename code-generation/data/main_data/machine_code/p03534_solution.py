def is_palindrome_possible(S):
    from collections import Counter
    count = Counter(S)
    
    if abs(count['a'] - count['b']) <= 1 and abs(count['b'] - count['c']) <= 1 and abs(count['a'] - count['c']) <= 1:
        return "YES"
    else:
        return "NO"

S = input()
print(is_palindrome_possible(S))