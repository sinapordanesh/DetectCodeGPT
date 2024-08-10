from heapq import heappop, heappush
def inpl(): return list(map(int, input().split()))

W, H = inpl()
INF = 10**6

while W:
    S = [[5]*(W+2)]
    for _ in range(H):
        S.append([5] + inpl() + [5])
    S.append([5]*(W+2))
    C = inpl()
    D = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    E = [[[INF]*4 for _ in range(W+2)] for _ in range(H+2)]
    E[1][1][1] = 0
    Q = [[0, 1, (1, 1)]]
    while Q:
        e, d, (w, h) = heappop(Q)
        order = S[h][w]
        if e > E[h][w][d] or order == 5:
            continue

        dw, dh = D[d]
        ne = e + C[0]*(order != 0)
        if E[h+dh][w+dw][d] > ne:
            E[h+dh][w+dw][d] = ne
            heappush(Q, [ne, d, (w+dw, h+dh)])

        nd = (d+1)%4
        dw, dh = D[nd]
        ne = e + C[1]*(order != 1)
        if E[h+dh][w+dw][nd] > ne:
            E[h+dh][w+dw][nd] = ne
            heappush(Q, [ne, nd, (w+dw, h+dh)])

        nd = (d+2)%4
        dw, dh = D[nd]
        ne = e + C[2]*(order != 2)
        if E[h+dh][w+dw][nd] > ne:
            E[h+dh][w+dw][nd] = ne
            heappush(Q, [ne, nd, (w+dw, h+dh)])

        nd = (d+3)%4
        dw, dh = D[nd]
        ne = e + C[3]*(order != 3)
        if E[h+dh][w+dw][nd] > ne:
            E[h+dh][w+dw][nd] = ne
            heappush(Q, [ne, nd, (w+dw, h+dh)])

    print(min(E[H][W]))
    W, H = inpl()
