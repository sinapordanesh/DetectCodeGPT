def sandglass(X, K, r_list, Q, queries):
    total_sand = X
    for t, a in queries:
        idx = 0
        sand_A = a
        for i in range(K):
            if t >= r_list[i]:
                if idx % 2 == 0:
                    sand_A += total_sand - a
                else:
                    sand_A = total_sand - sand_A
                idx += 1
        print(sand_A)