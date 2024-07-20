def biased_dice():
    while True:
        n = int(input())
        if n == 0:
            break
        result = [0, 0, 0, 0, 0, 0]
        for _ in range(n):
            t, f = map(int, input().split())
            if t == 1:
                result[5] += 1
            elif t == 2:
                result[4] += 1
            elif t == 3:
                result[3] += 1
            elif t == 4:
                if f == 1:
                    result[0] += 1
                elif f == 2:
                    result[1] += 1
                elif f == 3:
                    result[2] += 1
                elif f == 4:
                    result[5] += 1
                elif f == 5:
                    result[4] += 1
                else:
                    result[3] += 1
            elif t == 5:
                result[0] += 1
            else:
                result[1] += 1
        print(" ".join(map(str, result)))

biased_dice()