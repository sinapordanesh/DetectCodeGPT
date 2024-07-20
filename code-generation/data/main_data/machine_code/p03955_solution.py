def achievable(N, a):
    for i in range(1, N+1):
        if a[0][i-1] == i and a[1][i-1] == N+i and a[2][i-1] == 2*N+i:
            continue
        else:
            return "No"
    return "Yes"