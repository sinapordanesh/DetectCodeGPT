import sys

K, N = map(int, input().split())
P = 998244353


kaizyo = [0]
kaizyo_inv = [0]
tmp = 1
for i in range(1, N+K):
    tmp = (tmp*i) % P
    kaizyo.append(tmp)
    kaizyo_inv.append(pow(tmp, P - 2, P))


def comb(n, r):
    if n < r or r < 0:
        return 0
    elif n == r or r == 0:
        return 1
    else:
        return kaizyo[n] * kaizyo_inv[r] * kaizyo_inv[n - r]


inv_2 = pow(2, P - 2, P)
anss = ''
for i in range(2, 2 * K + 1):
    ans = 0
    n_pair = min((i - 1) // 2, (2 * K - i + 1) // 2)
    out_pair = max(0, K - i + 1, i - K - 1)
    which_use = pow(2, n_pair+1, P)
    for j in range(n_pair + 1):
        if n_pair - j > N:
            which_use = (which_use * inv_2) % P
            continue
        not_use = comb(n_pair, j)
        which_use = (which_use * inv_2) % P
        dice_cnt = comb(N - 1 + out_pair, n_pair - j - 1 + out_pair)
        if i % 2 == 0:
            dice_cnt = (dice_cnt + comb(N - 2 + out_pair,
                                        n_pair - j - 1 + out_pair)) % P
        tmp = (not_use * which_use) % P
        tmp = (tmp * dice_cnt) % P
        ans = (ans + tmp) % P
    anss += str(ans) + '\n'
print(anss.rstrip())
