def optimal_score(N, lotus):
    max_score = float('-inf')
    
    for A in range(1, N):
        B = (N - 1) % A
        score = 0
        current_pos = 0
        
        while current_pos != N - 1:
            y = current_pos + A
            if y == N - 1:
                score += lotus[y]
                break
            elif y < N and lotus[y] != 0:
                score += lotus[y]
                current_pos = y
            else:
                score -= 10**100
                break
            
            if current_pos != N - 1:
                y = current_pos - B
                if y == N - 1:
                    score += lotus[y]
                    break
                elif y >= 0 and lotus[y] != 0:
                    score += lotus[y]
                    current_pos = y
                else:
                    score -= 10**100
                    break
        
        max_score = max(max_score, score)
    
    return max_score

N = 5
lotus = [0, 2, 5, 1, 0]
print(optimal_score(N, lotus))

N = 6
lotus = [0, 10, -7, -4, -13, 0]
print(optimal_score(N, lotus))

N = 11
lotus = [0, -4, 0, -99, 31, 14, -15, -39, 43, 18, 0]
print(optimal_score(N, lotus))