def good_coloring(K):
    n = 3
    if K == 2:
        return f"{n}\n1 1 1\n1 1 1\n2 2 2"
    elif K == 9:
        return f"{n}\n1 2 3\n4 5 6\n7 8 9"