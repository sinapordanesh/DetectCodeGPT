K = 33
L = K * 2
s = [['#' for j in range(L)] for i in range(K)]
t = [['.' for j in range(L)] for i in range(K)]

A, B = map(int, input().split())

def color(s, j0, i1, c):
    j = j0
    k = j0 * 2
    for i in range(1, i1):
        if L <= k:
            j += 1
            k = (j & 1) << 1
        s[j][k] = c
        k += 4

color(s, 0, A, '.')
color(t, 1, B, '#')

print(L, L)
f = lambda s : print('\n'.join((map(lambda s : ''.join(s), s))))
f(s)
f(t)
