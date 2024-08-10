n, x, y, z = map(int, input().split())
mod = 10 ** 9 + 7
simple_xyz = (1 << (x + y + z - 1)) | (1 << (y + z - 1)) | (1 << (z - 1))
def isnotxyz(b):
    return b & simple_xyz != simple_xyz
dp = [[0] * (1 << (x + y + z - 1)) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for b in range(1 << (x + y + z - 1)):
        if dp[i][b] == 0:
            continue
        for j in range(10):
            # 右から10...0(0はj個)を付け足し、(x + y + z)桁目より左の情報は忘れる
            new_b = ((b << 1 | 1) << j) & ((1 << (x + y + z)) - 1)
            if isnotxyz(new_b):
                new_b &= (1 << (x + y + z - 1)) - 1
                dp[i + 1][new_b] += dp[i][b]
                dp[i + 1][new_b] %= mod
def summod(a, mod):
    res = 0
    for ai in a:
        res += ai
        res %= mod
    return res
#俳句的でないほうの数を求めたので、全体から引く
print((pow(10, n, mod) - sum(dp[n])) % mod)