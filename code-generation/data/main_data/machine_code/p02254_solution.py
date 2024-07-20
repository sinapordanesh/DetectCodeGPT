from collections import Counter

def huffman_coding_length(S):
    freq = Counter(S)
    total_length = 0
    
    while len(freq) > 1:
        x = freq.most_common()[-1][0]
        y = freq.most_common()[-2][0]
        
        new_node = x + y
        total_length += freq[x] + freq[y]
        
        del freq[x]
        del freq[y]
        
        freq[new_node] = freq[x] + freq[y]
    
    return total_length

S = input().strip()
print(huffman_coding_length(S))