def good_set_points(N, D1, D2):
    for i in range(N):
        for j in range(N):
            print(i*2, j*2)

        for i in range(N):
            for j in range(N):
                print(i*2+1, j*2+1)