def max_operations(S):
    count = 0
    for i in range(len(S)-1):
        if S[i] == 'B' and S[i+1] == 'W':
            count += 1
    return count

# Test the function with the provided samples
print(max_operations("BBW"))
print(max_operations("BWBWBW"))