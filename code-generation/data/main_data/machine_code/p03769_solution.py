def find_good_string(N):
    s = []
    while N > 0:
        s.append(1)
        N -= 2
    return len(s), ' '.join(map(str, s))