def equal_arcs_and_abcs(N, difficulties):
    difficulties.sort()
    middle = N // 2
    return len([k for k in difficulties if k > difficulties[middle - 1]])

N = 6
difficulties = [9, 1, 4, 4, 6, 7]
print(equal_arcs_and_abcs(N, difficulties))

N = 8
difficulties = [9, 1, 14, 5, 5, 4, 4, 14]
print(equal_arcs_and_abcs(N, difficulties))

N = 14
difficulties = [99592, 10342, 29105, 78532, 83018, 11639, 92015, 77204, 30914, 21912, 34519, 80835, 100000, 1]
print(equal_arcs_and_abcs(N, difficulties))