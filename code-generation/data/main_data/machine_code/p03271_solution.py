def can_reach_state(N, p):
    for i in range(1, N+1):
        if p[i-1] == i:
            continue
        if i+1 <= N and p[i-1] == i+1 and p[i] == i and p[i-2] == i-1:
            p[i-1], p[i], p[i-2] = p[i-2], p[i-1], p[i]
        else:
            return "No"
    return "Yes"