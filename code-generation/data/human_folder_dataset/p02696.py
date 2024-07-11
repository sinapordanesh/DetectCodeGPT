def f(a, b, n):
    if b == 1:
        print(0)
    else:
        Max = 0
        step = 1 if b // a ==  0 else b // a
        for x in range(b // a, n + step, step):
            res = (a * x) // b - a * (x // b)
            if res > Max:
                Max = res
        print(Max)

a, b, n = map(int, input().split()); f(a, b, n)
