def min_total_votes(N, votes):
    cur_t = 1
    cur_a = 1
    
    for i in range(N):
        ratio_t = votes[i][0] // cur_t
        ratio_a = votes[i][1] // cur_a
        
        times = max(ratio_t, ratio_a)
        
        cur_t = times * votes[i][0]
        cur_a = times * votes[i][1]
    
    return cur_t + cur_a