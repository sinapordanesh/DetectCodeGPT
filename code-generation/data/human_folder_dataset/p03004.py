import numpy as np

N = int(input())

x_min = [np.inf] * 4
x_max = [-np.inf] * 4
y_min = [np.inf] * 4
y_max = [-np.inf] * 4
for _ in range(N):
    x, y, d = input().split()
    x = int(x)
    y = int(y)
    i = {'R': 0, 'L': 1, 'U': 2, 'D': 3}[d]
    x_min[i] = min(x_min[i], x)
    x_max[i] = max(x_max[i], x)
    y_min[i] = min(y_min[i], y)
    y_max[i] = max(y_max[i], y)

x_max_ = max(x_max[2], x_max[3])
x_min_ = min(x_min[2], x_min[3])
y_max_ = max(y_max[0], y_max[1])
y_min_ = min(y_min[0], y_min[1])

def W(t):
    R = max(x_max[0] + t, x_max[1] - t, x_max_)
    L = min(x_min[0] + t, x_min[1] - t, x_min_)
    return R - L

def H(t):
    U = max(y_max[2] + t, y_max[3] - t, y_max_)
    D = min(y_min[2] + t, y_min[3] - t, y_min_)
    return U - D

def WH(t):
    return W(t) * H(t)

ts = [
    0,
    (x_max[1] - x_max[0]) / 2,
    (x_min[1] - x_min[0]) / 2,
    (y_max[3] - y_max[2]) / 2,
    (y_min[3] - y_min[2]) / 2,
    x_max_ - x_max[0],
    -(x_max_ - x_max[1]),
    x_min_ - x_min[0],
    -(x_min_ - x_min[1]),
    y_max_ - y_max[2],
    -(y_max_ - y_max[3]),
    y_min_ - y_min[2],
    -(y_min_ - y_min[3]),
]

result = np.inf;
for t in ts:
    if t >= 0:
        result = min(result, WH(t))

print(result)
