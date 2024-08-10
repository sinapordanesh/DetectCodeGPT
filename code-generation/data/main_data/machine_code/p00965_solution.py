def seats_required(n, lst):
    policy1 = 0
    policy2 = 0
    max_end = 0
    
    for i in range(n):
        start = lst[i][0]
        end = lst[i][1]
        
        if start <= max_end:
            policy1 += 1
        else:
            max_end = end
            policy1 += 1
    
    max_start = float('inf')
    min_end = float('-inf')
    for i in range(n):
        start = lst[i][0]
        end = lst[i][1]
        
        if start < max_start:
            max_start = start
        if end > min_end:
            min_end = end
    
    policy2 = min_end - max_start + 1
    
    return policy1, policy2