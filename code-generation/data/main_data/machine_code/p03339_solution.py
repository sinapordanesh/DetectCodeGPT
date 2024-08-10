def min_people_to_change_directions(N, S):
    count_west = S.count('W')
    count_east = S.count('E')
    min_change = min(count_west, count_east)
    
    return min_change