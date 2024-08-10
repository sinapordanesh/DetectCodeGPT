def max_persimmon_trees():
    while True:
        N = int(input())
        if N == 0:
            break
        persimmon_trees = []
        for _ in range(N):
            persimmon_trees.append(tuple(map(int, input().split())))
        W, H = map(int, input().split())
        S, T = map(int, input().split())
        max_trees = 0
        for i in range(W - S + 1):
            for j in range(H - T + 1):
                count = 0
                for tree in persimmon_trees:
                    if i <= tree[0] < i + S and j <= tree[1] < j + T:
                        count += 1
                max_trees = max(max_trees, count)
        print(max_trees)

max_persimmon_trees()