def fast_pow(x, y):
    if y == 0:
        return 1
    p = fast_pow(x, y // 2)
    p = p * p
    if y % 2:
        p = p * x
    return p


n, a = list(map(int, input().split()))
maxM = 1
d = 1
while n >= d:
    maxM += 1
    d *= 2

r = n
l = 0
while r - l > 1:
    mid = (r + l) // 2

    for m in range(2, maxM + 1):
        if (mid + a) % m == 0:
            if (mid + a) // m - a < 1:
                continue
            if fast_pow((mid + a) // m - a, m) >= n:
                r = mid
                break
        else:
            a1 = (mid + a + m - 1) // m - a
            a2 = (mid + a) // m - a
            if a1 < 1 or a2 < 1:
                continue

            if fast_pow(a1, (mid + a) % m) * fast_pow(a2, m - (mid + a) % m) >= n:
                r = mid
                break
    else:
        l = mid
print(r)
