def combinations_of_exits(N, M, robot_coords, exit_coords):
    MOD = 10**9 + 7
    return pow(2, min(N, M), MOD)