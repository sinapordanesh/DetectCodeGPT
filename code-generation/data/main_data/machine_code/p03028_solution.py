def count_possible_champions(N, results):
    possible_champions = set()
    for i in range(1, N+1):
        champions = set([i])
        for j in range(1, i):
            if results[i-1][j-1] == 1:
                champions.add(j)
            else:
                champions.add(i)
        possible_champions.update(champions)
    return len(possible_champions)