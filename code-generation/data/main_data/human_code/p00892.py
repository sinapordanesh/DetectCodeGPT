def width(_X, _Y, _n, _x):
    lb = float("inf")
    ub = -float("inf")

    for j in range(0, _n):
        x1 = _X[j]
        y1 = _Y[j]
        x2 = _X[(j + 1) % _n]
        y2 = _Y[(j + 1) % _n]

        if (x1 - _x) * (x2 - _x) <= 0 and x1 != x2:
            y = y1 + (y2 - y1) * (_x - x1) / (x2 - x1)
            lb = min(lb, y)
            ub = max(ub, y)

    return max(0, ub - lb)


if __name__ == '__main__':
    while True:
        M, N = list(map(int, input().split()))
        if M == 0 and N == 0:
            break

        X1 = []
        Y1 = []
        X2 = []
        Z2 = []
        for i in range(M):
            tmp_x1, tmp_y1 = list(map(int, input().split()))
            X1.append(tmp_x1)
            Y1.append(tmp_y1)

        for i in range(N):
            tmp_x2, tmp_z2 = list(map(int, input().split()))
            X2.append(tmp_x2)
            Z2.append(tmp_z2)

        min1 = min(X1)
        max1 = max(X1)
        min2 = min(X2)
        max2 = max(X2)

        xs = X1 + X2
        xs = sorted(xs)
        res = 0
        for i in range(0, len(xs) - 1):
            a = xs[i]
            b = xs[i + 1]
            c = (a + b) / 2
            # print("a" + str(a) + "b" + str(b) + "c" + str(c))
            if min1 <= c <= max1 and min2 <= c <= max2:
                fa = width(X1, Y1, M, a) * width(X2, Z2, N, a)
                fb = width(X1, Y1, M, b) * width(X2, Z2, N, b)
                fc = width(X1, Y1, M, c) * width(X2, Z2, N, c)
                res += ((b - a) / 6) * (fa + 4 * fc + fb)
                # print(res)

        print(res)