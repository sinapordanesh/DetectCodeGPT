def pattern_search():
    H, W = map(int, input().split())
    region = [input() for _ in range(H)]
    R, C = map(int, input().split())
    pattern = [input() for _ in range(R)]

    for i in range(H - R + 1):
        for j in range(W - C + 1):
            if all(region[i+k][j:j+C] == pattern[k] for k in range(R)):
                print(i, j)

pattern_search()