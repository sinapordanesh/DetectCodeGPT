def min_stones_needed(S):
    black_count = S.count('B')
    white_count = S.count('W')
    return abs(black_count - white_count)

#Sample Input
print(min_stones_needed("BBBWW"))
print(min_stones_needed("WWWWWW"))
print(min_stones_needed("WBWBWBWBWB"))