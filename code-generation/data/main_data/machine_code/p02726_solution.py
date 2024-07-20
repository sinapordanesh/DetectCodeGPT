def shortest_distance_pairs(N, X, Y):
    for k in range(1, N):
        if k < Y - X:
            print(k)
        elif Y - X + 1 <= k < Y + X:
            print(Y - X + 1)
        else:
            print(N - k - 1)