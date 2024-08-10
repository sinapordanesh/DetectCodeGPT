def line_gimmick(N, S):
    panels_removed = 0
    current_index = 0
    
    while current_index < N:
        panels_removed += 1
        if S[current_index] == '<':
            current_index += 1
        else:
            current_index = N - current_index - 1
    
    return panels_removed