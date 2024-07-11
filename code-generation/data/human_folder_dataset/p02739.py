res = []

n = int(input())
a = [int(c) for c in input()]

def solve():
    if a[0] == 0:
        return False
    for x in range(1, 2**n):
        s = list(filter(lambda i: (x >> i) & 1, range(n)))
        xl = [(x >> i) & 1 for i in range(n)]
        if a[x] == 0:
            for d in s:
                y = x ^ (1 << d)
                if a[y] == 1:
                    break
            else:
                continue
            def move_ceiling(r, dest):
                i, j = r[-1]
                if i < dest:
                    for i in range(i, dest):
                        if xl[i] == 0 and j == 1:
                            r.append((i, 0))
                            j = 0
                        elif xl[i] == 1 and j == 0:
                            r.append((i, 1))
                            j = 1
                        r.append((i + 1, j))
                else:
                    for i in range(i, dest, -1):
                        if xl[i - 1] == 0 and j == 1:
                            r.append((i, 0))
                            j = 0
                        elif xl[i - 1] == 1 and j == 0:
                            r.append((i, 1))
                            j = 1
                        r.append((i - 1, j))
                return r
            def move_floor(r, dest):
                i, j = r[-1]
                if j == 1:
                    r.append((i, 0))
                for i in range(i + 1, dest + 1) if i < dest else range(i - 1, dest - 1, -1):
                    r.append((i, 0))
                return r
            r = [(s[0] + 1, 1), (s[0], 1), (s[0], 0), (s[0] + 1, 0)]
            cur = s[0] + 1
            for d in s[1:]:
                r0 = [(d + 1, 1)] if cur == d else move_ceiling([(d + 1, 1)], cur)
                r1 = move_ceiling(r.copy(), d + 1)
                r1 = move_floor(r1, cur)
                r1.pop()
                r2 = list(reversed(r))
                r2 = move_floor(r2, d + 1)
                r = r0 + r1 + r2
                cur = d + 1
            r = move_floor(r, n)
            r.reverse()
            r = move_floor(r, n)
            r.pop()
            res.append(r)
        else:
            for d in s:
                y = x ^ (1 << d)
                if a[y] != 1:
                    return False
    return True

if __name__ == '__main__':
    if solve():
        print('Possible')
        r = [(i, j) for r in res for i, j in r]
        r.append((n, 0))
        print(len(r) - 1)
        for i, j in r:
            print(i, j)
    else:
        print('Impossible')
