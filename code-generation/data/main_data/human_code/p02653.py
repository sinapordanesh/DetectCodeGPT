def solve(n, a, b):
    MOD = 10 ** 9 + 7
    if a > b:
        a, b = b, a
    if a == 1:
        return pow(2, n, MOD)

    # 長さ i の区間であり、右端が '1' であり、
    # はじめ '1' で塗りつぶされていたのを、
    # 長さ a 以上の '0' で0回以上上書きすることで実現できる並びの個数
    dp1 = [0] * (b + 1)
    dp1_acc = [0] * (b + 1)
    dp1[0] = 1
    dp1_acc[0] = 1

    for i in range(1, b + 1):
        tmp = dp1[i - 1]  # 末尾に1を付ける
        if i - a - 1 >= 0:
            tmp = (tmp + dp1_acc[i - a - 1]) % MOD  # 末尾に 00..01 を付ける
        dp1[i] = tmp
        dp1_acc[i] = (dp1_acc[i - 1] + tmp) % MOD
    # 派生情報
    # dp1[i-1]: 長さ i の区間であり、「両端」が'1'であるものの個数
    # dp1[i] - dp1[i-1]: 長さ i の区間であり、左端が'0'、右端が'1'（またはその逆）のものの個数

    # dp2x[i]
    # 長さ i の区間であり、末尾が x であり、
    # 長さa以上の'0'も、長さb以上の'1'も含まない01の並びの個数
    # ただし'1'は、dp1で求めたように、その内部をa個以上の'0'で置きかえたものも含む
    dp20 = [0] * (n + 1)
    dp21 = [0] * (n + 1)
    dp21_acc = [0] * (n + 1)
    dp20[0] = dp21[0] = dp21_acc[0] = 1
    for i in range(1, n + 1):
        t0 = dp21_acc[i - 1]
        if i >= a:
            t0 -= dp21_acc[i - a]
        dp20[i] = t0 % MOD

        t1 = 0
        for j in range(1, min(i + 1, b)):
            t1 += dp20[i - j] * dp1[j - 1]
        # 左端が '111...' でb個以上取れないもので、さらに'0'で置きかえられた結果、最左端が'0'のもの
        if i < b:
            t1 += dp1[i] - dp1[i - 1]
        t1 %= MOD
        dp21[i] = t1
        dp21_acc[i] = (dp21_acc[i - 1] + t1) % MOD

    disable = dp20[n] + dp21[n]

    # 最後が'111..'でb個以上取れないもので、
    # さらに'0'で置きかえられた結果、右端が'0'のものが数えられていない
    for i in range(1, b):
        disable += dp20[n - i] * (dp1[i] - dp1[i - 1])

    return (pow(2, n, MOD) - disable) % MOD


n, a, b = map(int, input().split())
print(solve(n, a, b))
