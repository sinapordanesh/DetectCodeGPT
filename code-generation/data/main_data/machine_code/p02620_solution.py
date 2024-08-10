def fast_incremental_score_calculation(D, c, s, t, M, queries):
    satisfaction = []
    
    def calculate_satisfaction(t):
        total_satisfaction = 0
        for d in range(D):
            total_satisfaction += s[d][t[d]-1]
        return total_satisfaction
    
    current_satisfaction = calculate_satisfaction(t)
    satisfaction.append(current_satisfaction)
    
    for i in range(M):
        d, q = queries[i]
        old_type = t[d-1]
        t[d-1] = q
        new_satisfaction = calculate_satisfaction(t)
        
        if new_satisfaction < current_satisfaction:
            t[d-1] = old_type
        else:
            current_satisfaction = new_satisfaction
        
        satisfaction.append(current_satisfaction)
    
    return satisfaction

# Sample input
D = 5
c = [86, 90, 69, 51, 2, 96, 71, 47, 88, 34, 45, 46, 89, 34, 31, 38, 97, 84, 41, 80, 14, 4, 50, 83, 7, 82]
s = [[19771, 12979, 18912, 10432, 10544, 12928, 13403, 3047, 10527, 9740, 8100, 92, 2856, 14730, 1396, 15905, 6534, 4650, 11469, 3628, 8433, 2994, 10899, 16396, 18355, 11424],
     [6674, 17707, 13855, 16407, 12232, 2886, 11908, 1705, 5000, 1537, 10440, 10711, 4917, 10770, 17272, 15364, 19277, 18094, 3929, 3705, 7169, 6159, 18683, 15410, 9092, 4570],
     [6878, 4239, 19925, 1799, 375, 9563, 3445, 5658, 19857, 11401, 6997, 6498, 19933, 3848, 2426, 2146, 19745, 16880, 17773, 18359, 3921, 14172, 16730, 11157, 5439, 256],
     [8633, 15862, 15303, 10749, 18499, 7792, 10317, 5901, 9395, 11433, 3514, 3959, 5202, 19850, 19469, 9790, 5653, 784, 18500, 10552, 17975, 16615, 7852, 197, 8471, 7452],
     [19855, 17918, 7990, 10572, 4333, 438, 9140, 9104, 12622, 4985, 12319, 4028, 19922, 12132, 16259, 17476, 2976, 547, 19195, 19830, 16285, 4806, 4471, 9457, 2864, 2192]]
t = [1, 17, 13, 14, 13]
M = 5
queries = [(1, 7), (4, 11), (3, 4), (5, 24), (4, 19)]

print(*fast_incremental_score_calculation(D, c, s, t, M, queries))