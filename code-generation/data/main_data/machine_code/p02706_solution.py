def max_days_hang_out(N, M, assignments):
    total_days = sum(assignments)
    if total_days > N:
        return -1
    return N - total_days
    