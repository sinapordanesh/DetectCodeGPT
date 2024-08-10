def can_learn_special_commands(M, N, conditions):
    skills = [0] * N
    
    for i in range(M):
        K = conditions[i][0]
        for j in range(1, K+1):
            skill = conditions[i][j][0]
            cond = conditions[i][j][1]
            threshold = conditions[i][j][2]
            
            if cond == '<=':
                if skills[skill-1] > threshold:
                    return "No"
            elif cond == '>=':
                if skills[skill-1] < threshold:
                    return "No"
            
        for j in range(1, K+1):
            skill = conditions[i][j][0]
            skills[skill-1] = max(skills[skill-1], conditions[i][j][2])
    
    return "Yes"