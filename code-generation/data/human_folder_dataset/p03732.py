import sys
from itertools import accumulate

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, W, *WV = map(int, read().split())
    weight = WV[::2]
    value = WV[1::2]

    w0 = weight[0]
    items = [[] for _ in range(4)]
    for w, v in zip(weight, value):
        items[w - w0].append(v)

    for i in range(4):
        items[i].sort(reverse=True)

    csums = [0] * 4
    for i in range(4):
        csums[i] = [0]
        csums[i].extend(accumulate(items[i]))

    def rec(i, w, v):
        if i == 4:
            return v
        ans = 0
        w_next = w
        for j in range(len(csums[i])):
            if w_next > W:
                break
            ans = max(ans, rec(i + 1, w_next, v + csums[i][j]))
            w_next += w0 + i

        return ans

    print(rec(0, 0, 0))
    return


if __name__ == '__main__':
    main()
