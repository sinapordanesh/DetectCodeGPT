from collections import defaultdict
def main(h, w, s):
    u = [None] * h
    acc = [None] * (h + 1)
    acc[0] = [0] * (w + 1)
    for i in range(h):
        x = list(map(int, input().split()))
        acc[i + 1] = [0] + x
        u[i] = x
    for i in range(h):
        acci1 = acc[i + 1]
        for j in range(w):
            acci1[j + 1] += acci1[j]
    for i in range(h):
        acci = acc[i]
        acci1 = acc[i + 1]
        for j in range(w):
            acci1[j + 1] += acci[j + 1]
    dp = defaultdict(int)
    allsum = acc[-1][-1]
    def accsum(l, r, d, u):
        return acc[u + 1][r + 1] - acc[u + 1][l] - acc[d][r + 1] + acc[d][l]
    for wm in range(w):
        for hm in range(h):
            for l in range(w - wm):
                r = l + wm
                for d in range(h - hm):
                    u = d + hm
                    ac = accsum(l, r, d, u)
                    res = [1, s - (allsum - ac)]
                    for mw in range(l, r):
                        tmp1 = dp[(l, mw, d, u)]
                        tmp2 = dp[(mw + 1, r, d, u)]
                        if tmp1[1] >= 0 and tmp2[1] >= 0:
                            tmp = [tmp1[0] + tmp2[0], min(tmp1[1], tmp2[1])]
                            if tmp[0] > res[0]:
                                res = tmp
                            elif tmp[0] == res[0] and tmp[1] > res[1]:
                                res = tmp
                    for mh in range(d, u):
                        tmp1 = dp[(l, r, d, mh)]
                        tmp2 = dp[(l, r, mh + 1, u)]
                        if tmp1[1] >= 0 and tmp2[1] >= 0:
                            tmp = [tmp1[0] + tmp2[0], min(tmp1[1], tmp2[1])]
                            if tmp[0] > res[0]:
                                res = tmp
                            elif tmp[0] == res[0] and tmp[1] > res[1]:
                                res = tmp
                    dp[(l, r, d, u)] = res
    print(*dp[(0, w - 1, 0, h - 1)])

if __name__ == '__main__':
    while 1:
        h, w, s = map(int, input().split())
        if h == w == s == 0:
            break
        main(h, w, s)


