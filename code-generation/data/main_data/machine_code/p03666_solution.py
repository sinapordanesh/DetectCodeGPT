def fill_squares(N, A, B, C, D):
    if (B-A) <= D*N and (B-A) >= C*N:
        return "YES"
    else:
        return "NO"