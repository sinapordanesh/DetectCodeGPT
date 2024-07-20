def shortest_common_non_subsequence(seq1, seq2):
    common_non_subsequence = []
    i, j = 0, 0
    
    while i < len(seq1) and j < len(seq2):
        if seq1[i] != seq2[j]:
            common_non_subsequence.append('0')
            i += 1
            j += 1
        else:
            common_non_subsequence.append(seq1[i])
            i += 1
            j += 1
    
    while i < len(seq1):
        common_non_subsequence.append(seq1[i])
        i += 1
        
    while j < len(seq2):
        common_non_subsequence.append(seq2[j])
        j += 1
        
    return ''.join(common_non_subsequence)