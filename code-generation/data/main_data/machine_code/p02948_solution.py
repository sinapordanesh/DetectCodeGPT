def max_total_reward(N, M, jobs):
    jobs.sort(key=lambda x: x[0])
    total_reward = 0
    days = 0
    idx = 0
    
    while days < M and idx < N:
        if jobs[idx][0] > days:
            total_reward += jobs[idx][1]
            days += 1
        idx += 1
    
    return total_reward

# Sample Input 1
print(max_total_reward(3, 4, [[4, 3], [4, 1], [2, 2]]))

# Sample Input 2
print(max_total_reward(5, 3, [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3]]))

# Sample Input 3
print(max_total_reward(1, 1, [[2, 1]]))