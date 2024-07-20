def ab_problem():
    a, b = map(int, input().split())
    d = a // b
    r = a % b
    f = a / b
    print(d, r, "{:.5f}".format(f))

ab_problem()