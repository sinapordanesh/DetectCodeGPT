def max_score(N, K, R, S, P, T):
    score = 0
    prev_hands = []
    
    for i in range(N):
        if i < K or T[i-K] == 'r':
            score += P if T[i] == 's' else S if T[i] == 'r' else R
        elif i < K or T[i-K] == 's':
            score += R if T[i] == 'p' else P if T[i] == 's' else S
        elif i < K or T[i-K] == 'p':
            score += S if T[i] == 'r' else R if T[i] == 'p' else P
        
        prev_hands.append(T[i])
    
    return score

N, K, R, S, P, T = map(int, input().split())
print(max_score(N, K, R, S, P, T))