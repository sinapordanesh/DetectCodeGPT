def trampoline(N, distances):
    current = distances[0]
    for i in range(N-1):
        if current >= N-1:
            return "yes"
        current = max(current-1, distances[i+1])
        
    if current >= N-1:
        return "yes"
    
    current = distances[-1]
    for i in range(N-1, 0, -1):
        if current >= N-i:
            return "yes"
        current = max(current-1, distances[i-1])
    
    return "no"