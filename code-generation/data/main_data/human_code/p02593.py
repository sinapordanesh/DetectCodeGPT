import os
import sys

import numpy as np


def solve(inp):
    n = inp[0]
    xxx = inp[1::2]
    yyy = inp[2::2]
    xxx_idx = np.argsort(xxx)
    yyy_idx = np.argsort(yyy)
    # print('xxx_idx', xxx_idx)
    # print('yyy_idx', yyy_idx)
    xxx_num = np.argsort(xxx_idx)
    yyy_num = np.argsort(yyy_idx)

    # print('xxx_num', xxx_num)
    # print('yyy_num', yyy_num)

    # i: 入力順のルークの番号
    # xi: x座標昇順にソートしたときの順番
    # xxx_idx[xi] = i
    # xxx_num[i] = xi

    def get_xy_by_xi(xi):
        i = xxx_idx[xi]
        return xxx[i], yyy[i]

    def calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, lpxi, rnxi, rook_cnt):
        lpx, lpy = get_xy_by_xi(lpxi)
        rnx, rny = get_xy_by_xi(rnxi)

        diag_t = abs(rnx - lpx) + abs(rny - lpy) - rook_cnt

        lllt = llt + abs(rnx - lx) + abs(rny - ly) + diag_t
        llrt = llt + abs(lx - lpx) + abs(ly - lpy) + diag_t
        lrlt = lrt + abs(rnx - rx) + abs(rny - ry) + diag_t
        lrrt = lrt + abs(rx - lpx) + abs(ry - lpy) + diag_t
        rllt = rlt + abs(rnx - lx) + abs(rny - ly) + diag_t
        rlrt = rlt + abs(lx - lpx) + abs(ly - lpy) + diag_t
        rrlt = rrt + abs(rnx - rx) + abs(rny - ry) + diag_t
        rrrt = rrt + abs(rx - lpx) + abs(ry - lpy) + diag_t

        llt = min(lllt, lrlt)
        lrt = min(llrt, lrrt)
        rlt = min(rllt, rrlt)
        rrt = min(rlrt, rrrt)
        # print('upd', lpx, lpy, rnx, rny)
        # print('upd', llt, lrt, rlt, rrt)
        # print('upd', lllt, llrt, lrlt, lrrt, rllt, rlrt, rrlt, rrrt)

        return lpx, lpy, rnx, rny, llt, lrt, rlt, rrt

    # free[xi] = xi+1 のルークと初期状態から互いに取り合える関係にあるか(0/1)
    free = np.zeros(n, dtype=np.int8)

    for i in range(n):
        xi = xxx_num[i]
        yi = yyy_num[i]
        px_i = -1 if xi == 0 else xxx_idx[xi - 1]
        nx_i = -2 if xi == n - 1 else xxx_idx[xi + 1]
        py_i = -3 if yi == 0 else yyy_idx[yi - 1]
        ny_i = -4 if yi == n - 1 else yyy_idx[yi + 1]
        if px_i == py_i or px_i == ny_i:
            free[xi - 1] = 1
        if nx_i == py_i or nx_i == ny_i:
            free[xi] = 1

    # freeが連続する箇所は、どこから始めても互いに全て取り合える
    # これを「グループ」とする
    # グループの左端と右端のxiを求める
    free_l = np.zeros(n, dtype=np.int64)
    free_r = np.zeros(n, dtype=np.int64)
    l = 0
    for xi in range(n - 1):
        if free[xi] == 0:
            l = xi + 1
        free_l[xi + 1] = l
    r = n - 1
    free_r[r] = r
    for xi in range(n - 2, -1, -1):
        if free[xi] == 0:
            r = xi
        free_r[xi] = r

    # print(free)
    # print(free_l)
    # print(free_r)

    # グループ内のルークを全部取った時点を0として、追加で取れるルークを取るのにかかる時間
    # グループ内のルークを取り終わったのが、左端、右端のいずれかで2通り計算
    # 同グループに属するルークはこの情報を共有できるので、一番左端のルークの位置に記録
    # Key: xi
    extra_l = np.zeros(n, dtype=np.int64)
    extra_r = np.zeros(n, dtype=np.int64)
    INF = 10 ** 18
    lxi = 0
    while lxi < n:
        rxi = free_r[lxi]

        if lxi == rxi:
            lxi = rxi + 1
            continue

        li = xxx_idx[lxi]
        ri = xxx_idx[rxi]
        lyi = yyy_num[li]
        ryi = yyy_num[ri]
        lyi, ryi = min(lyi, ryi), max(lyi, ryi)

        original_li = lxi
        lx = xxx[li]
        ly = yyy[li]
        rx = xxx[ri]
        ry = yyy[ri]
        llt, lrt, rlt, rrt = 0, INF, INF, 0

        # print('li', li, 'ri', ri, 'lxi', lxi, 'lyi', lyi, 'rxi', rxi, 'ryi', ryi)

        while True:
            px_i = -1 if lxi == 0 else xxx_idx[lxi - 1]
            py_i = -2 if lyi == 0 else yyy_idx[lyi - 1]
            nx_i = -3 if rxi == n - 1 else xxx_idx[rxi + 1]
            ny_i = -4 if ryi == n - 1 else yyy_idx[ryi + 1]
            # print(px_i, py_i, nx_i, ny_i)
            if px_i == py_i:
                lpxi = free_l[lxi - 1]
                rook_cnt = lxi - lpxi

                if nx_i == ny_i:
                    rnxi = free_r[rxi + 1]
                    rook_cnt += rnxi - rxi
                    # print(0, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                    lx, ly, rx, ry, llt, lrt, rlt, rrt = \
                        calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, lpxi, rnxi, rook_cnt)
                    lxi = lpxi
                    rxi = rnxi
                    uyi = yyy_num[xxx_idx[lxi]]
                    vyi = yyy_num[xxx_idx[rxi]]
                    lyi, ryi = min(lyi, ryi, uyi, vyi), max(lyi, ryi, uyi, vyi)
                    # print(0, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                else:
                    # print(1, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                    lx, ly, rx, ry, llt, lrt, rlt, rrt = \
                        calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, lpxi, lpxi, rook_cnt)
                    lxi = lpxi
                    uyi = yyy_num[xxx_idx[lxi]]
                    lyi, ryi = min(lyi, ryi, uyi), max(lyi, ryi, uyi)
                    # print(1, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)

            elif px_i == ny_i:
                lpxi = free_l[lxi - 1]
                rook_cnt = lxi - lpxi

                if nx_i == py_i:
                    rnxi = free_r[rxi + 1]
                    rook_cnt += rnxi - rxi
                    # print(2, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                    lx, ly, rx, ry, llt, lrt, rlt, rrt = \
                        calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, lpxi, rnxi, rook_cnt)
                    lxi = lpxi
                    rxi = rnxi
                    uyi = yyy_num[xxx_idx[lxi]]
                    vyi = yyy_num[xxx_idx[rxi]]
                    lyi, ryi = min(lyi, ryi, uyi, vyi), max(lyi, ryi, uyi, vyi)
                    # print(2, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                else:
                    # print(3, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, llt, lrt, rlt, rrt)
                    lx, ly, rx, ry, llt, lrt, rlt, rrt = \
                        calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, lpxi, lpxi, rook_cnt)
                    lxi = lpxi
                    uyi = yyy_num[xxx_idx[lxi]]
                    lyi, ryi = min(lyi, ryi, uyi), max(lyi, ryi, uyi)
                    # print(3, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, llt, lrt, rlt, rrt)

            elif nx_i == ny_i or nx_i == py_i:
                rnxi = free_r[rxi + 1]
                rook_cnt = rnxi - rxi
                # print(4, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)
                lx, ly, rx, ry, llt, lrt, rlt, rrt = \
                    calc_time(lx, ly, rx, ry, llt, lrt, rlt, rrt, rnxi, rnxi, rook_cnt)
                rxi = rnxi
                vyi = yyy_num[xxx_idx[rxi]]
                lyi, ryi = min(lyi, ryi, vyi), max(lyi, ryi, vyi)
                # print(4, lxi, rxi, lyi, ryi, '|', lx, ly, rx, ry, lt, rt)

            else:
                extra_l[original_li] = min(llt, lrt)
                extra_r[original_li] = min(rlt, rrt)
                break

        lxi = rxi + 1

    # print(extra_l)
    # print(extra_r)

    ans = np.zeros(n, dtype=np.int64)
    for i in range(n):
        xi = xxx_num[i]
        x = xxx[i]
        y = yyy[i]
        lxi = free_l[xi]
        lx = xxx[xxx_idx[lxi]]
        ly = yyy[xxx_idx[lxi]]
        rxi = free_r[xi]
        rx = xxx[xxx_idx[rxi]]
        ry = yyy[xxx_idx[rxi]]
        lt = extra_l[lxi]
        rt = extra_r[lxi]
        diag = abs(rx - lx) + abs(ry - ly) - (rxi - lxi)
        rlt = abs(rx - x) + abs(ry - y) + diag
        lrt = abs(x - lx) + abs(y - ly) + diag
        ans[i] = min(lt + rlt, rt + lrt)

    return ans


if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', '(i8[:],)')(solve)
    cc.compile()
    exit()

if os.name == 'posix':
    # noinspection PyUnresolvedReferences
    from my_module import solve
else:
    from numba import njit

    solve = njit('(i8[:],)', cache=True)(solve)
    print('compiled', file=sys.stderr)

inp = np.fromstring(sys.stdin.read(), dtype=np.int64, sep=' ')
ans = solve(inp)
print('\n'.join(map(str, ans)))
