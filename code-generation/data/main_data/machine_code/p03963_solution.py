def paint_balls(N, K):
    if N == 1:
        return K
    elif N == 2:
        return K * (K-1)
    else:
        return K * ((K-1) ** (N-1))