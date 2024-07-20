import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def longest_increasing_subsequence(seq):
    side = 'left'
    N = len(seq)
    INF = 10**18
    dp = np.full_like(seq, INF)
    for x in seq:
        i = np.searchsorted(dp, x, side)
        dp[i] = x
    return np.searchsorted(dp, INF - 1, side)

if sys.argv[-1] == 'ONLINE_JUDGE':
    import numba
    from numba.pycc import CC
    i8 = numba.from_dtype(np.int64)
    signature = (i8[:], )

    cc = CC('my_module')
    cc.export('longest_increasing_subsequence',
              signature)(longest_increasing_subsequence)
    cc.compile()

from my_module import longest_increasing_subsequence

x1, y1, x2, y2 = map(int, readline().split())
N = int(readline())
XY = np.array(read().split(), np.int64)

X = XY[::2]
Y = XY[1::2]

if x1 > x2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1
if y1 > y2:
    y1, y2 = -y1, -y2
    Y = -Y

X -= x1
Y -= y1
x = x2 - x1
y = y2 - y1

cond = (X >= 0) & (X<=x) & (Y>=0) & (Y<=y)
X = X[cond]
Y = Y[cond]
ind = np.argsort(X)
X = X[ind]
Y = Y[ind]

n = longest_increasing_subsequence(Y)

answer = x+y
answer -= (0.2 - 0.1 * np.pi/2) * n
if n == min(x,y) + 1:
    answer += 0.1 * np.pi / 2
answer *= 100
print(answer)