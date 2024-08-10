def find_nearest_integer(X, N, sequence):
    sequence_set = set(sequence)
    result = float('inf')
    min_diff = float('inf')
    
    if X not in sequence_set:
        return X
    
    for i in range(1, 102):
        if i not in sequence_set:
            diff = abs(X - i)
            if diff < min_diff:
                min_diff = diff
                result = i
                
    return result
                

# Sample Input 1
X1 = 6
N1 = 5
sequence1 = [4, 7, 10, 6, 5]
print(find_nearest_integer(X1, N1, sequence1))

# Sample Input 2
X2 = 10
N2 = 5
sequence2 = [4, 7, 10, 6, 5]
print(find_nearest_integer(X2, N2, sequence2))

# Sample Input 3
X3 = 100
N3 = 0
sequence3 = []
print(find_nearest_integer(X3, N3, sequence3))