def can_complete_problem_set(N, D, M, T):
    if len(set(D)) >= M:
        return "YES"
    else:
        return "NO"