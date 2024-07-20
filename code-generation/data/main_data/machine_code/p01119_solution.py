def balance_scale(n, m, amounts, weights):
    total = sum(amounts)
    if total % 2 != 0:
        return -1
    target = total // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for w in weights:
        for i in range(target, w - 1, -1):
            dp[i] |= dp[i - w]

    for i in range(target, -1, -1):
        if dp[i]:
            return total - 2 * i

    return -1