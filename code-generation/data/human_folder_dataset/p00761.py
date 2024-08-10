def solve(n, l):
    results = [n]
    for i in range(20):
        s = list(("%0" + str(l) + "d") % n)
        s.sort()
        n = int("".join(s[::-1])) - int("".join(s))
        if n in results:
            break
        results.append(n)
    j = results.index(n)
    print(j, n, i - j + 1)

while True:
    n, l = map(int, input().split())
    if n == l == 0:
        break
    solve(n, l)

