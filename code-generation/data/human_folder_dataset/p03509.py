from itertools import accumulate


def solve(l, r):
    if l > r:
        return l
    m = (l + r) // 2
    w, b = whites[m], blues[m]
    if w * 100 // (w + b) < p:
        l = m + 1
    else:
        r = m - 1
    return solve(l, r)


n, p = map(int, input().split())
wbs = [tuple(map(int, input().split())) for _ in range(n)]
ass = [(w * (100 - p) + b * p, i) for i, (w, b) in enumerate(wbs)]
ass.sort(reverse=True)
whites = list(accumulate(wbs[i][0] for _, i in ass))
blues = [wbs[i][1] for _, i in ass[1:]]
blues = list(reversed(list(accumulate(reversed(blues))))) + [0]

# print(list(whites))
# print(list(blues))
print(solve(0, n - 1) + 1)
