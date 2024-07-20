def white_bird_solver(N, V, X, Y, obstacles):
    for obstacle in obstacles:
        L, B, R, T = obstacle
        if (X - V**2/(2*9.8) >= L) and (X + V**2/(2*9.8) <= R) and (Y >= B) and (Y <= T):
            return "No"
    return "Yes"