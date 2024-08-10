def assignment_possible(N, p_list):
    for i in range(N):
        if i in p_list:
            if p_list.count(i) > 1:
                return "POSSIBLE"
    return "IMPOSSIBLE"