def possible_cats(A, B, X):
    if X <= A + B and X >= A:
        return "YES"
    else:
        return "NO"