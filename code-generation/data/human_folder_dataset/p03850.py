def solve(n, inp):
    if n == 1:
        return int(inp[0])

    INF = -(10 ** 18)

    dp1, dp2, dp3 = int(inp[0]), INF, INF
    for op, a in zip(inp[1::2], inp[2::2]):
        a = int(a)
        if op == '+':
            dp1, dp2, dp3 = dp1 + a, max(dp2 - a, dp3 + a), dp3 + a
        else:
            dp1, dp2, dp3 = max(dp1 - a, dp2 + a), max(dp1 - a, dp2 + a), max(dp2 + a, dp3 - a)

    return dp1


n = int(input())
inp = input().split()
print(solve(n, inp))
