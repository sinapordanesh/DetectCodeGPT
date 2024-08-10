def max_satisfied_desires(N, K, desires):
    black = {}
    white = {}
    for x, y, c in desires:
        if c == 'B':
            if (x//K, y//K) not in black:
                black[(x//K, y//K)] = 0
            black[(x//K, y//K)] += 1
        else:
            if (x//K, y//K) not in white:
                white[(x//K, y//K)] = 0
            white[(x//K, y//K)] += 1
    max_satisfied = 0
    for count in black.values():
        max_satisfied = max(max_satisfied, count)
    for count in white.values():
        max_satisfied = max(max_satisfied, count)
    return max_satisfied