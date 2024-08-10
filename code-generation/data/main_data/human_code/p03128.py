def main():
    n, m = map(int, input().split())
    a = set(map(int, input().split()))

    # type(x) == type(y) == string
    def bigger(x, y):
        if len(x) > len(y):
            return x
        elif len(x) < len(y):
            return y
        elif x < y:
            return y
        else:
            return x

    l = []
    if 1 in a:
        l.append((2, '1'))

    if 7 in a:
        l.append((3, '7'))

    if 4 in a:
        l.append((4, '4'))

    if 5 in a:
        l.append((5, '5'))
    elif 3 in a:
        l.append((5, '3'))
    elif 2 in a:
        l.append((5, '2'))

    if 9 in a:
        l.append((6, '9'))
    elif 6 in a:
        l.append((6, '6'))

    if 8 in a:
        l.append((7, '8'))

    dp = [None] * (n+1)
    dp[0] = ''
    for i in range(1, n+1):
        for cost, char in l:
            if i - cost < 0 or dp[i-cost] is None:
                continue
            candidate = max(dp[i-cost] + char, char + dp[i-cost])
            if dp[i] is None:
                dp[i] = candidate
            else:
                dp[i] = bigger(dp[i], candidate)

    print(dp[n])

main()