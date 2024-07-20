def min_tiles_repainted(S):
    count = 0
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            count += 1
    return count

# Test the function with the sample inputs
print(min_tiles_repainted("000"))
print(min_tiles_repainted("10010010"))
print(min_tiles_repainted("0"))