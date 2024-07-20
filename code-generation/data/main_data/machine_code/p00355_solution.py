def check_overlap(a, b, N, reservations):
    for i in range(N):
        if (a < reservations[i][1] and b > reservations[i][0]):
            return 1
    return 0