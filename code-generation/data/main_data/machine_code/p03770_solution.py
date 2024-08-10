def sequence_of_colors(N, X, Y, balls):
    MOD = 10**9 + 7
    colors = set()
    
    for i in range(N):
        for j in range(i+1, N):
            if balls[i][0] == balls[j][0] and balls[i][1] + balls[j][1] <= X:
                colors.add(tuple(balls))
            elif balls[i][0] != balls[j][0] and balls[i][1] + balls[j][1] <= Y:
                colors.add(tuple(sorted(balls)))
            
    return len(colors) % MOD