def shuttle_run(N, M, yokans):
    yokans.sort()
    total_distance = 0
    current_position = 0
    
    for yokan in yokans:
        if current_position < yokan[0]:
            total_distance += 2 * (yokan[0] - current_position)
            current_position = yokan[1]
        elif current_position > yokan[1]:
            total_distance += 2 * (current_position - yokan[1])
            current_position = yokan[0]
    
    if current_position > 0:
        total_distance += 2 * current_position
    
    return total_distance