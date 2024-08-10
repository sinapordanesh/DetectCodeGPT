#!/usr/bin/python3

import array
import os
import sys


def main():
    S = inp()
    T = inp()
    print(solve(S, T))


def solve(S, T):
    sn = len(S)
    tn = len(T)

    sd = [[sn + 1] * (sn + 1), [sn + 1] * (sn + 1)]
    for i in range(sn):
        idx = ord(S[i]) - ord('0')
        for j in range(i, -1, -1):
            if sd[idx][j] != sn + 1:
                break
            sd[idx][j] = i + 1
    td = [[tn + 1] * (tn + 1), [tn + 1] * (tn + 1)]
    for i in range(tn):
        idx = ord(T[i]) - ord('0')
        for j in range(i, -1, -1):
            if td[idx][j] != tn + 1:
                break
            td[idx][j] = i + 1
    #dprint('sd', sd)
    #dprint('td', td)

    sb = [[[] for _ in range(sn + 2)] for _ in range(2)]
    for b in (0, 1):
        for i in range(sn + 1):
            sb[b][sd[b][i]].append(i)
        sb[b][sn + 1].append(sn + 1)
    tb = [[[] for _ in range(tn + 2)] for _ in range(2)]
    for b in (0, 1):
        for i in range(tn + 1):
            tb[b][td[b][i]].append(i)
        tb[b][tn + 1].append(tn + 1)
    #dprint('sb', sb)
    #dprint('tb', tb)

    INF = max(sn, tn) + 2
    arr_temp = [INF] * (tn + 2)
    dists = [array.array('i', arr_temp) for _ in range(sn + 2)]
    q = set()
    q.add((sn + 1, tn + 1))
    d = 0
    while q:
        nq = set()
        for i, j in q:
            if dists[i][j] != INF:
                continue
            dists[i][j] = d
            for b in (0, 1):
                for ni in sb[b][i]:
                    for nj in tb[b][j]:
                        if dists[ni][nj] == INF and (ni, nj) not in q:
                            nq.add((ni, nj))
        d += 1
        q = nq

    #dprint('dists', dists)

    ans = []
    i, j = 0, 0
    d = dists[0][0]
    while (i, j) != (sn + 1, tn + 1):
        #dprint('->', i, j)
        ni = sd[0][i] if i < sn + 1 else sn + 1
        nj = td[0][j] if j < tn + 1 else tn + 1
        if dists[ni][nj] == d - 1:
            ans.append('0')
        else:
            ans.append('1')
            ni = sd[1][i] if i < sn + 1 else sn + 1
            nj = td[1][j] if j < tn + 1 else tn + 1
        i = ni
        j = nj
        d -= 1

    return ''.join(ans)


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


if __name__ == '__main__':
    main()

