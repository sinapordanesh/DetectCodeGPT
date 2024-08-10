def maximum_score(N, K, P, C):
    max_score = float('-inf')
    
    for i in range(1, N+1):
        visited = [False] * N
        score = [0]
        cur = i
        moves = 1
        
        while not visited[cur-1]:
            visited[cur-1] = True
            cur = P[cur-1]
            score.append(score[-1] + C[cur-1])
            moves += 1
            
            if moves > K:
                break
        
        if moves <= K:
            cycle_score = score[-1] - score[0]
            cycle_length = moves - 1
            remaining_moves = K - moves
            
            if cycle_score > 0:
                max_score = max(max_score, score[-1] + (remaining_moves // cycle_length) * cycle_score)
            
            for j in range(1, moves):
                remaining_moves -= 1
                max_score = max(max_score, score[j] + (remaining_moves // cycle_length) * cycle_score)
    
    return max_score

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
print(maximum_score(N, K, P, C))