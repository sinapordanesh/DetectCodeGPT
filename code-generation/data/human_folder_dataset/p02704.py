def numba_compile(numba_config):
    import os, sys
    if sys.argv[-1] == "ONLINE_JUDGE":
        from numba import njit
        from numba.pycc import CC
        cc = CC("my_module")
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature)(func)
            cc.export(func.__name__, signature)(func)
        cc.compile()
        exit()
    elif os.name == "posix":
        exec(f"from my_module import {','.join(func.__name__ for func, _ in numba_config)}")
        for func, _ in numba_config:
            globals()[func.__name__] = vars()[func.__name__]
    else:
        from numba import njit
        for func, signature in numba_config:
            globals()[func.__name__] = njit(signature, cache=True)(func)
        print("compiled!", file=sys.stderr)


import numpy as np

def solve_1bit(N, rps, cps, rv, cv):
    res = np.full((N, N), 2, dtype=np.uint64)
    if N == 1:
        res[0, 0] = rv[0]
        return res
    r_all = np.array([False, False])
    for i, (ps, v) in enumerate(zip(rps, rv)):
        if ps ^ v == 1:
            res[i, :] = v
            r_all[v] = True
    c_all = np.array([False, False])
    for i, (ps, v) in enumerate(zip(cps, cv)):
        if ps ^ v == 1:
            res[:, i] = v
            c_all[v] = True
    if (r_all[0] and c_all[1]) or (r_all[1] and c_all[0]):
        return res
    if r_all[0] and c_all[0]:
        return np.where(res==2, np.uint64(1), res)
    if r_all[1] and c_all[1]:
        return np.where(res==2, np.uint64(0), res)
    if np.all(r_all):
        for y in range(N):
            for x in range(N):
                if res[y, x] == 2:
                    res[y, x] = rv[y]
        return res
    if np.all(c_all):
        for y in range(N):
            for x in range(N):
                if res[y, x] == 2:
                    res[y, x] = cv[x]
        return res
    if r_all[0]:
        if (cv==0).any():
            x = (cv==0).nonzero()[0][0]
            res[:, x] = 0
            return np.where(res==2, np.uint64(1), res)
        x = 0
        for y in range(N):
            v = rv[y]
            if v == 0 and res[y, 0] == 2:
                res[y, x] = 0
                x = (x+1) % N
        return np.where(res==2, np.uint64(1), res)
    if r_all[1]:
        if (cv==1).any():
            x = (cv==1).nonzero()[0][0]
            res[:, x] = 1
            return np.where(res==2, np.uint64(0), res)
        x = 0
        for y in range(N):
            v = rv[y]
            if v == 1 and res[y, 0] == 2:
                res[y, x] = 1
                x = (x+1) % N
        return np.where(res==2, np.uint64(0), res)
    if c_all[0]:
        if (rv==0).any():
            y = (rv==0).nonzero()[0][0]
            res[y, :] = 0
            return np.where(res==2, np.uint64(1), res)
        y = 0
        for x in range(N):
            v = cv[x]
            if v == 0 and res[0, x] == 2:
                res[y, x] = 0
                y = (y+1) % N
        return np.where(res==2, np.uint64(1), res)
    if c_all[1]:
        if (rv==1).any():
            y = (rv==1).nonzero()[0][0]
            res[y, :] = 1
            return np.where(res==2, np.uint64(0), res)
        y = 0
        for x in range(N):
            v = cv[x]
            if v == 1 and res[0, x] == 2:
                res[y, x] = 1
                y = (y+1) % N
        return np.where(res==2, np.uint64(0), res)
    for y in range(N):
        for x in range(N):
            res[y, x] = (y^x)&1
    return res

def solve(N, row_prod_sum, col_prod_sum, row_val, col_val):
    res = np.zeros((N, N), dtype=np.uint64)
    for i in range(64):
        rps = row_prod_sum
        cps = col_prod_sum
        rv = row_val>>i&1
        cv = col_val>>i&1
        r = solve_1bit(N, rps, cps, rv, cv)
        res |= r<<i
    #print(res)
    prod = res[0].copy()
    sum_ = res[0].copy()
    for y in range(1, N):
        prod &= res[y]
        sum_ |= res[y]
    #print(prod, sum_)
    if (prod[col_prod_sum==0] != col_val[col_prod_sum==0]).any():
        return 0, np.array([[-1]], dtype=np.int64)
    if (sum_[col_prod_sum==1] != col_val[col_prod_sum==1]).any():
        return 0, np.array([[-1]], dtype=np.int64)
    prod = res[:, 0].copy()
    sum_ = res[:, 0].copy()
    for x in range(1, N):
        prod &= res[:, x]
        sum_ |= res[:, x]
    #print(prod, sum_)
    if (prod[row_prod_sum==0] != row_val[row_prod_sum==0]).any():
        return 0, np.array([[-1]], dtype=np.int64)
    if (sum_[row_prod_sum==1] != row_val[row_prod_sum==1]).any():
        return 0, np.array([[-1]], dtype=np.int64)
    return 1, res


numba_compile([
    [solve_1bit, "u8[:,:](i8,u8[:],u8[:],u8[:],u8[:])"],
])


def main():
    N = int(input())
    row_prod_sum = np.array(input().split(), dtype=np.uint64)
    col_prod_sum = np.array(input().split(), dtype=np.uint64)
    row_val = np.array(input().split(), dtype=np.uint64)
    col_val = np.array(input().split(), dtype=np.uint64)
    t, ans = solve(N, row_prod_sum, col_prod_sum, row_val, col_val)
    if t:
        for lst in ans.tolist():
            print(" ".join(map(str, lst)))
    else:
        print(-1)

main()
