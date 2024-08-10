def beautiful_spacing(W, N, x):
    spaces = []
    line_length = 0
    for i in range(N):
        line_length += x[i]
        if i != N-1:
            line_length += 1
        if line_length > W:
            spaces.append(line_length - x[i] - (1 if i != N-1 else 0))
            line_length = x[i]
    spaces.append(line_length - (1 if N != 1 else 0))
    
    return max(spaces) - 1 - (W - sum(x) - len(x) + 1) // (N-1) if N != 1 else W - sum(x)