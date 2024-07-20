def is_objective_achievable(A, B, C):
    if C % math.gcd(A, B) == 0:
        return "YES"
    else:
        return "NO"