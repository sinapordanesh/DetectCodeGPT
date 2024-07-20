def max_illumination(dataset):
    N, M, R = dataset[0]
    balloons = dataset[1:N+1]
    lights = dataset[N+1:N+M+1]
    objective_point = dataset[N+M+1]
    
    def calculate_intensity(balloons, lights, objective_point):
        total_intensity = 0
        for light in lights:
            x_l, y_l, z_l, b = light
            distance = (x_l - objective_point[0])**2 + (y_l - objective_point[1])**2 + (z_l - objective_point[2])**2
            intensity = b / distance
            for balloon in balloons:
                x_b, y_b, z_b, r = balloon
                if (x_l - x_b)**2 + (y_l - y_b)**2 + (z_l - z_b)**2 < r**2:
                    intensity = 0
                    break
            total_intensity += intensity
        return total_intensity
    
    def remove_balloon(balloons, index):
        return balloons[:index] + balloons[index+1:]
    
    def backtrack(balloons, lights, objective_point, R, index):
        if R == 0 or index == len(balloons):
            return calculate_intensity(balloons, lights, objective_point)
        remove_current = backtrack(remove_balloon(balloons, index), lights, objective_point, R-1, index)
        keep_current = backtrack(balloons, lights, objective_point, R, index+1)
        return max(remove_current, keep_current)
    
    return backtrack(balloons, lights, objective_point, R, 0)