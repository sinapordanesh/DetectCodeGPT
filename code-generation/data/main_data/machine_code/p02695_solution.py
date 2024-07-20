def max_score(N, M, Q, queries):
    def helper(curr_seq):
        score = 0
        for query in queries:
            a, b, c, d = query
            if curr_seq[b-1] - curr_seq[a-1] == c:
                score += d
        return score
    
    def generate_sequences(curr_seq, remaining):
        if len(curr_seq) == N:
            return helper(curr_seq)
        
        max_score = 0
        for i in range(curr_seq[-1], M+1):
            max_score = max(max_score, generate_sequences(curr_seq + [i], remaining-1))
        
        return max_score
    
    max_score = 0
    for i in range(1, M+1):
        max_score = max(max_score, generate_sequences([i], N-1))
    
    return max_score

# Input
N, M, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(Q)]

# Output
print(max_score(N, M, Q, queries))