def longest_hidden_anagrams(s1, s2):
    def is_anagram(s, t):
        return sorted(s) == sorted(t)
    
    max_length = 0
    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            if len(s1[i:j]) < max_length:
                continue
            for k in range(len(s2)):
                for l in range(k + 1, len(s2) + 1):
                    if is_anagram(s1[i:j], s2[k:l]):
                        max_length = max(max_length, len(s1[i:j]))
    return max_length

# Test cases
print(longest_hidden_anagrams("anagram", "grandmother"))
print(longest_hidden_anagrams("williamshakespeare", "iamaweakishspeller"))
print(longest_hidden_anagrams("aaaaaaaabbbbbbbb", "xxxxxabababxxxxxabab"))
print(longest_hidden_anagrams("abababacdcdcd", "efefefghghghghgh"))