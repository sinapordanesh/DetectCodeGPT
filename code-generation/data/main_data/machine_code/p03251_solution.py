def will_war_break_out(N, M, X, Y, x, y):
    if min(y) < X < min(y) and max(x) < Y <= max(y):
        return "No War"
    else:
        return "War"