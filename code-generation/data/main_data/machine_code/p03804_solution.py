def is_template_contained(N, M, A, B):
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if all(A[i + k][j:j+M] == B[k] for k in range(M)):
                return "Yes"
    return "No"