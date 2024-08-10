def water_tank_simulation(D, data_sets):
    results = []
    
    for data in data_sets:
        N = data[0]
        boards = data[1:N+1]
        M = data[N+1]
        faucets = data[N+2:N+2+M]
        L = data[N+2+M]
        observation_points = data[N+3+M:]
        
        tank_height = 50
        tank_width = 100
        tank_depth = 30
        tank = [tank_height] * tank_width
        
        for faucet in faucets:
            x_pos, flow_rate = faucet
            for t in range(L):
                for i in range(x_pos, tank_width):
                    tank[i] += flow_rate
        
        for obs_point in observation_points:
            obs_x, obs_time = obs_point
            water_level = min(tank[obs_x], tank_height)
            results.append(water_level)
    
    return results