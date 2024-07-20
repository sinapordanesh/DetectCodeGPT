def where_is_wally():
    while True:
        w, h, p = map(int, input().split())
        if w == 0 and h == 0 and p == 0:
            break
        image = [input() for _ in range(h)]
        pattern = [input() for _ in range(p)]

        def count_occurrences(image, pattern):
            count = 0
            for i in range(h - p + 1):
                for j in range(w - p + 1):
                    match = True
                    for x in range(p):
                        for y in range(p):
                            if image[i+x][j+y] != pattern[x][y]:
                                match = False
                                break
                        if not match:
                            break
                    if match:
                        count += 1
            return count

        print(count_occurrences(image, pattern))

where_is_wally()