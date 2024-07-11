def solve(a, b):
    if a == b:
        return 1

    f = 1 << 60
    r = 0
    while f:
        if r == 0 and b & f and a & f == 0:
            r = f
        elif r > 0 and b & f:
            k = f << 1
            break
        f >>= 1
    else:
        k = 1

    a &= r - 1

    if k > a:
        return (r << 1) - a

    return 2 * (r - a) + k


a = int(input())
b = int(input())
print(solve(a, b))
