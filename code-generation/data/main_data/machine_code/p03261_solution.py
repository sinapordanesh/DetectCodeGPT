def shiritori(N, words):
    used_words = set()
    prev_word = words[0]
    used_words.add(prev_word)
    
    for i in range(1, N):
        if words[i] in used_words or words[i][0] != prev_word[-1]:
            return "No"
        used_words.add(words[i])
        prev_word = words[i]
    
    return "Yes"