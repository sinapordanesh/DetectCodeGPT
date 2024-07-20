def is_achievable(N, edges_blue, edges_red):
    if N == 2:
        return "YES"
    else:
        return "YES" if N % 2 == 0 else "NO"