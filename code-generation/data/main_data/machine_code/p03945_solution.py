def min_stones_needed(S):
    count = 0
    if S[0] == S[-1]:
        count = 1
    
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            count += 1
    
    return count

# Sample Input 1
print(min_stones_needed("BBBWW"))

# Sample Input 2
print(min_stones_needed("WWWWWW"))

# Sample Input 3
print(min_stones_needed("WBWBWBWBWB"))