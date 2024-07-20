def can_have_exact_black_squares(N, M, K):
    for i in range(N+1):
        for j in range(M+1):
            if K == (N-i)*j + i*(M-j):
                return "Yes"
    return "No"