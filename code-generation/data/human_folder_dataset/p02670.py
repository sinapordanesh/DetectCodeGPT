import sys
import numpy as np

def main(N, P):
    minDist = np.ones((N, N), dtype=np.int32)
    isFilled = np.ones((N, N), dtype=np.int32)

    for h in range(N):
        for w in range(N):
            minDist[h][w] = min(h, N - h - 1, w, N - w - 1)

    ans = 0
    dh = (1, -1, 0, 0)
    dw = (0, 0, 1, -1)
    for p in P:
        h, w = divmod(p, N)
        ans += minDist[h][w]
        isFilled[h][w] = 0

        st = [(h, w)]
        while st:
            h, w = st.pop()
            dist = minDist[h][w] + isFilled[h][w]

            for i in range(4):
                toH, toW = h + dh[i], w + dw[i]
                if 0 <= toH < N and 0 <= toW < N:
                    if minDist[toH][toW] > dist:
                        minDist[toH][toW] = dist
                        st.append((toH, toW))
    return ans

def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main', 'i4(i4, i4[:])')(main)
    cc.compile()

if sys.argv[-1] == 'ONLINE_JUDGE':
    cc_export()
    exit(0)
if sys.argv[-1] != 'LOCAL':
    from my_module import main

N = int(input())
P = np.asarray(list(map(lambda a: int(a) - 1, input().split())), dtype=np.int32)

print(main(N, P))
