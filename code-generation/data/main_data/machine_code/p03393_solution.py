def next_diverse_word(S):
    if len(S) == 26:
        return -1
    
    for i in range(len(S)-1, -1, -1):
        if ord(S[i]) - ord('a') < 25:
            return S[:i] + chr(ord(S[i]) + 1) + 'a' * (len(S) - i - 1)
    
    return S + 'a'