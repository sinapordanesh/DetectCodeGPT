def num_problems_chosen(N, M, V, P, A):
    A.sort(reverse=True)
    threshold_score = A[P-1]
    problems_with_chance = 0
    for i in range(N):
        if i < P-1:
            if A[i] >= threshold_score:
                problems_with_chance += 1
        else:
            if A[i] + M >= threshold_score and A[i] > 0:
                problems_with_chance += 1
    return problems_with_chance