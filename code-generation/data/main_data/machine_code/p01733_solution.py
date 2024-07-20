def fox_observation(N, foxes):
    total_foxes = sum([fox[2] for fox in foxes])
    max_value = 0
    
    for i in range(N):
        for j in range(i+1, N):
            x_diff = abs(foxes[i][0] - foxes[j][0])
            y_diff = abs(foxes[i][1] - foxes[j][1])
            observed_foxes = sum([fox[2] for fox in foxes if foxes[i][0] <= fox[0] <= foxes[j][0] and foxes[i][1] <= fox[1] <= foxes[j][1]])
            value = observed_foxes / (x_diff * y_diff)
            max_value = max(max_value, value)
    
    return f"{int(max_value)} / 1" if max_value.is_integer() else f"{int(max_value*10)} / 10"