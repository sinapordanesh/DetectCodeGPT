def find_unbalanced_substring(s):
    n = len(s)
    
    for i in range(n-1):
        for j in range(i+1, n):
            substring = s[i:j+1]
            count = {}
            for char in substring:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            max_count = max(count.values())
            if len(substring) >= 2 and max_count > len(substring) // 2:
                return i+1, j+1
                
    return -1, -1