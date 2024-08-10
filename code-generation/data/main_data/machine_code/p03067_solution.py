def straight_way(A, B, C):
    if A <= C <= B or A >= C >= B:
        return "Yes"
    else:
        return "No"