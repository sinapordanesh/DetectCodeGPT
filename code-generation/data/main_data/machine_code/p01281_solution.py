def count_possible_ways():
    while True:
        h, w = map(int, input().split())
        if h == 0 and w == 0:
            break
        count = 0
        for i in range(h):
            for j in range(w):
                if i % 2 == 0 and j % 2 == 0:
                    count += 1
        print(count)

count_possible_ways()