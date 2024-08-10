def piece_remain_on_grid(H, W, N, s_r, s_c, S, T):
    r, c = s_r, s_c
    for i in range(N):
        if S[i] == 'L' and c > 1:
            c -= 1
        elif S[i] == 'R' and c < W:
            c += 1
        elif S[i] == 'U' and r > 1:
            r -= 1
        elif S[i] == 'D' and r < H:
            r += 1
        
        if T[i] == 'L' and c < W:
            c += 1
        elif T[i] == 'R' and c > 1:
            c -= 1
        elif T[i] == 'U' and r < H:
            r += 1
        elif T[i] == 'D' and r > 1:
            r -= 1
        
    if r > 0 and r <= H and c > 0 and c <= W:
        return "YES"
    else:
        return "NO"