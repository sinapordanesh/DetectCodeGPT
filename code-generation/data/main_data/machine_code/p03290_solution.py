def min_problems_needed(D, G, p, c):
    ans = float('inf')
    
    for i in range(1 << D):
        score = 0
        problems = 0
        rest_max = -1
        
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j + 1) * p[j] + c[j]
                problems += p[j]
            else:
                rest_max = j
        
        if score < G:
            need = (G - score + 100 * (rest_max + 1) - 1) // (100 * (rest_max + 1))
            if need >= p[rest_max]:
                continue
            problems += need
        
        ans = min(ans, problems)
    
    return ans