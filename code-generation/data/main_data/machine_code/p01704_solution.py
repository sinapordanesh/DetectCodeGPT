def min_cost():
    while True:
        N = int(input())
        if N == 0:
            break
        pw = int(input())
        flowers = []
        for _ in range(N):
            vw, pf, vf, th = map(int, input().split())
            flowers.append((vw, pf, vf, th))

        def calc_cost(w, fs):
            return w * pw + sum(f[1] * f[2] * f[0] for f in zip(fs, flowers))

        def check(w, fs):
            for f, (_, pf, vf, th) in zip(fs, flowers):
                if w * f + pf * vf >= th:
                    continue
                return False
            return True

        def ternary_search(low, high):
            for _ in range(200):
                m1 = (low * 2 + high) / 3
                m2 = (low + high * 2) / 3
                if calc_cost(m1, flowers) < calc_cost(m2, flowers):
                    high = m2
                else:
                    low = m1
            return calc_cost(low, flowers)

        low, high = 0, 1000
        print(ternary_search(low, high))

min_cost()