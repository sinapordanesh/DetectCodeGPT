def distribution_center(n, m, robot_arms):
    lanes = [0] * n
    for x, y in robot_arms:
        lanes[y-1] += 1
        lanes[y] += 1
    return lanes