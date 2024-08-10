def solve_problem():
    N = int(input())
    total = N
    res = []
    for i in range(1, N+1):
        if total - i > i:
            res.append(i)
            total -= i
    for r in res:
        print(r)