def possible_bills(N, Y):
    for x in range(N+1):
        for y in range(N-x+1):
            z = N - x - y
            if 10000*x + 5000*y + 1000*z == Y:
                return f"{x} {y} {z}"
    return "-1 -1 -1"