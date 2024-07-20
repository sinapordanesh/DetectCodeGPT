def is_possible(S):
    from collections import Counter
    count = Counter(S)
    
    if len(S) == 1:
        return "YES"
    
    if any(value >= len(S)//2 + 1 for value in count.values()):
        return "NO"
    
    return "YES"