def construct_tree(N, D):
    if sum(D) != 2*(N-1):
        print(-1)
    else:
        for i in range(1, N):
            print(i, i+1)