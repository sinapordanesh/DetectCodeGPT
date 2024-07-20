def find_triple(N):
    for h in range(1, 3501):
        for n in range(1, 3501):
            if 4/N - 1/h - 1/n != 0:
                continue
            w = 4/N - 1/h - 1/n
            if w.is_integer() and w > 0 and w <= 3500:
                return h, n, int(w)

N = int(input())
h, n, w = find_triple(N)
print(h, n, w)