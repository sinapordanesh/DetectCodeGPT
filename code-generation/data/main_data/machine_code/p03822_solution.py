def min_depth_tournament(N, a):
    depth = 0
    for i in range(2, N+1):
        cur_depth = 1
        j = i
        while j != 1:
            j = a[j-2]
            cur_depth += 1
        depth = max(depth, cur_depth)
    return depth