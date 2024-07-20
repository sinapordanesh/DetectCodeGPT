def can_visit_all_towns(a1, b1, a2, b2, a3, b3):
    if (a1 in [1, 2] and b1 in [1, 2]) and (a2 in [1, 2] and b2 in [1, 2]) and (a3 in [1, 2] and b3 in [1, 2]):
        return "YES"
    else:
        return "NO"