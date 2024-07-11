# Ref: https://betrue12.hateblo.jp/entry/2020/07/12/060026
import sys
sys.setrecursionlimit(10**6)


def ext_euc(a, b):
    if b == 0:
        return 1, 0, a
    y, x, v = ext_euc(b, a % b)
    y -= (a // b) * x
    return x, y, v


def mod_inv(a, mod):
    x, _, _ = ext_euc(a, mod)
    return x % mod


def generate_points(is_odd, mod):
    # Lagrange補完するためのデータ点を計算
    n_points = 16
    points = [None] * n_points
    if is_odd:
        comb_1 = [0] * n_points  # (n+4)_C_4
        comb_2 = [0] * n_points  # (2n+10)_C_10
        comb_1[0] = 1
        comb_2[0] = 1
        for n in range(1, n_points):
            comb_1[n] = comb_1[n - 1] * (n + 4) * mod_inv(n, mod) % mod
            v = comb_2[n - 1] * (2 * n + 10) * (2 * n + 9) % mod
            v *= mod_inv(2 * n, mod) * mod_inv(2 * n - 1, mod) % mod
            comb_2[n] = v % mod
        for n in range(n_points):
            N = 2 * n + 5
            val = 0
            for k in range(n + 1):
                val += comb_1[k] * comb_2[n - k]
                val %= mod
            points[n] = (N, val)
    else:
        comb_1 = [0] * n_points  # (k+4)_C_4
        comb_2 = [0] * n_points  # (2n+11)_C_10
        comb_1[0] = 1
        comb_2[0] = 11  # 11_C_10
        for n in range(1, n_points):
            comb_1[n] = comb_1[n - 1] * (n + 4) * mod_inv(n, mod) % mod
            v = comb_2[n - 1] * (2 * n + 11) * (2 * n + 10) % mod
            v *= mod_inv(2 * n + 1, mod) * mod_inv(2 * n, mod) % mod
            comb_2[n] = v % mod
        for n in range(n_points):
            N = 2 * n + 6
            val = 0
            for k in range(n + 1):
                val += comb_1[k] * comb_2[n - k]
                val %= mod
            points[n] = (N, val)
    return points


def lagrange_interpolation(points, k, mod):
    n_points = len(points)
    # points を通る n_points - 1 次の多項式 の k での値を求める
    # ref: https://mathtrain.jp/hokan
    ret = 0
    for n in range(n_points):
        x, y = points[n]
        y_coef = 1
        for i in range(n_points):
            if i == n:
                continue
            xi, _ = points[i]
            y_coef *= k - xi
            y_coef *= mod_inv(x - xi, mod)
        ret += y * y_coef
        ret %= mod
    return ret


def main():
    MOD = 10**9 + 7
    T = int(input())
    test_cases = [int(input()) for _ in range(T)]
    odd_points = generate_points(True, MOD)
    even_points = generate_points(False, MOD)
    for N in test_cases:
        if N < 5:
            print(0)
        elif N % 2 == 0:
            print(lagrange_interpolation(even_points, N, MOD))
        else:
            print(lagrange_interpolation(odd_points, N, MOD))


if __name__ == '__main__':
    main()
