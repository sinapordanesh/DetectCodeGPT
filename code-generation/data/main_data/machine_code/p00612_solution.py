def fdp_tiles_needed(N):
    if N == 0:
        return
    return N**3 * 3

# Sample Input
print(fdp_tiles_needed(2))
print(fdp_tiles_needed(4))