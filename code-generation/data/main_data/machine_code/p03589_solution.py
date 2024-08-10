def triple_of_integers(N):
    for h in range(1, 3501):
        for n in range(1, 3501):
            if (4/N - 1/h - 1/n) != 0:
                w = int(1 / (4/N - 1/h - 1/n))
                if (4/N - 1/h - 1/n - 1/w) == 0 and w <= 3500:
                    return h, n, w

N = int(input())
h, n, w = triple_of_integers(N)
print(h, n, w)