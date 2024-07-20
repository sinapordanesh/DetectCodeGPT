def construct_tree(N, a):
    a.sort()
    for i in range(N):
        if a[i] > i:
            return "Impossible"
    return "Possible"