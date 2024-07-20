def search_i(n, S, q, T):
    count = 0
    for num in T:
        if num in S:
            count += 1
    return count