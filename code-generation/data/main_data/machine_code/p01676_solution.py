def tree_reconstruction():
    while True:
        try:
            N, M = map(int, input().split())
            print(N - 1)
            for _ in range(M):
                input()
        except:
            break

tree_reconstruction()