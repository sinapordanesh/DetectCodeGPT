import random
from collections import defaultdict


def solve(n, s, xs, m):
    ans = [10 ** 9] * (n + 1)
    for x in xs:
        p = 0
        h = 0
        y = 1
        r = pow(x, m - 2, m)
        pos = [0] * (n + 1)
        hashes = [0] * (n + 1)
        for i, c in enumerate(s, start=1):
            if c == '>':
                p += 1
                y = y * x % m
            elif c == '<':
                p -= 1
                y = y * r % m
            elif c == '+':
                h = (h + y) % m
            else:
                h = (h - y) % m
            pos[i] = p
            hashes[i] = h

        pow_x = [1]
        for _ in range(max(pos)):
            pow_x.append(pow_x[-1] * x % m)
        mp = min(pos)
        if mp < 0:
            pow_x.append(pow(r, -mp, m))
            for _ in range(-mp - 1):
                pow_x.append(pow_x[-1] * x % m)

        ideal = hashes[-1]
        required = defaultdict(lambda: 0)
        for i, (p, h) in enumerate(zip(pos, hashes)):
            ans[i] = min(ans[i], required[h])
            req = (ideal * pow_x[p] + h) % m
            required[req] += 1

    return sum(ans)


n = int(input())
s = input()

xs = random.sample(range(10 ** 9, 10 ** 10), 3)
m = 2305843009213693951
print(solve(n, s, xs, m))
