def is_achievable(N, A, B, C, D, S):
    def can_reach(start, end, S):
        if start < end:
            return '.' in S[start:end+1] and '#' not in S[start:end+1]
        else:
            return '.' in S[end:start+1] and '#' not in S[end:start+1]
    
    if (can_reach(A-1, C-1, S) and can_reach(B-1, D-1, S)) or (can_reach(A-1, D-1, S) and can_reach(B-1, C-1, S)):
        return "Yes"
    else:
        return "No"

N, A, B, C, D = map(int, input().split())
S = input()
print(is_achievable(N, A, B, C, D, S))