def sort_pairs():
    n = int(input())
    pairs = []
    for _ in range(n):
        x, y = map(int, input().split())
        pairs.append((x, y))
    pairs.sort(key=lambda pair: (pair[0], pair[1]))
    for pair in pairs:
        print(pair[0], pair[1]) 

sort_pairs()