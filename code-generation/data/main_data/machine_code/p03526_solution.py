def max_participants(N, participants):
    participants.sort(reverse=True)
    count = 0
    stack_height = [0] * (N+1)
    
    for i in range(N):
        for j in range(N, 0, -1):
            if participants[i][0] > stack_height[j]:
                stack_height[j] = stack_height[j-1] + participants[i][1]
                count = max(count, j)
                break
                
    return count