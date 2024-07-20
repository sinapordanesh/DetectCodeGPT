def check_curve(R, C, N, points):
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                continue
            else:
                return "YES"
    return "NO"