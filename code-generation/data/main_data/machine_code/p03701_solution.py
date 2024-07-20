def max_displayed_grade(N, scores):
    max_grade = sum(scores)
    if max_grade % 10 == 0:
        return max_grade - min(scores)
    return max_grade