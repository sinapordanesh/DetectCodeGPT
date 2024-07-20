import numpy as np

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = np.array(A, dtype=float)
b = np.array(B, dtype=float)

argmaxA = a.argmax()
a = np.roll(a, -argmaxA)
b = np.roll(b, -argmaxA + 1)
a = np.append(a, a[0])
b = np.append(b, b[0])
bb = np.cumsum(b)
c = 2 * np.cumsum(bb)

# force a_c[0]==a_c[N]==0
c -= c[0]
c -= np.arange(N + 1) * ((c[-1] - c[0]) / (N))
c += a[0]

a_c = a - c


def signed_area(x1, y1, x2, y2, x3, y3):
    x12 = x2 - x1
    y12 = y2 - y1
    x13 = x3 - x1
    y13 = y3 - y1
    return x12 * y13 - x13 * y12


# convex hull O(n)
vertices = [(0, a_c[0]), (1, a_c[1])]
for i in range(2, N + 1):
    while (
        len(vertices) >= 2 and signed_area(*vertices[-2], *vertices[-1], i, a_c[i]) >= 0
    ):
        vertices.pop()

    vertices.append((i, a_c[i]))

ans = 0
for i in range(len(vertices) - 1):
    ans += (vertices[i + 1][0] - vertices[i][0]) * (vertices[i + 1][1] + vertices[i][1])
ans /= N * 2
ans += c[:-1].mean()
print(ans)