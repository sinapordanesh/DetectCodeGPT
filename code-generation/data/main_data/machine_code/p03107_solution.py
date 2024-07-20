def max_cubes_removed(S):
    count = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            count += 1
    return count

# Test the function with sample inputs
print(max_cubes_removed("0011"))
print(max_cubes_removed("11011010001011"))
print(max_cubes_removed("0"))