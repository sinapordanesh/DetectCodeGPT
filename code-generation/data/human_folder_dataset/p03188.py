def solve(k):
    if k == 1:
        print(1)
        print(1)
        return

    n = ((k - 1) // 4 + 1) * 2
    ans = [[0] * n for _ in [0] * n]
    dub = 2 * (k - n)
    for m in range(n * 2):
        l = m + 1 if m < dub else dub + (m - dub) // 2 + 1
        i = m % 2
        j = (m // 2 + m % 2) % n

        for _ in range(n // 2):
            ans[i][j] = l
            i = (i + 2) % n
            j = (j + 2) % n

    print(n)
    print('\n'.join(' '.join(map(str, row)) for row in ans))


k = int(input())
solve(k)
