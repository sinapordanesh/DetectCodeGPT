def shower_water(N, T, times):
    total_time = 0
    prev_time = 0
    
    for time in times:
        if time - prev_time < T:
            total_time += time - prev_time
        else:
            total_time += T
        
        prev_time = time
    
    total_time += T  # Add T seconds for the last person
    return total_time