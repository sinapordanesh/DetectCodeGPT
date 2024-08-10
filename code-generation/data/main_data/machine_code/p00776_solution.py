def decode_encrypted_string(encrypted_string):
    candidates = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(encrypted_string)):
        current_letter = encrypted_string[i]
        if current_letter == 'a':
            candidates.append(encrypted_string)
        else:
            new_string = encrypted_string[:i] + alphabet[alphabet.index(current_letter) - 1] + encrypted_string[i + 1:]
            candidates.append(new_string)
    
    candidates.sort()
    
    if len(candidates) <= 10:
        return len(candidates), candidates
    else:
        return 10, candidates[:5] + candidates[-5:]