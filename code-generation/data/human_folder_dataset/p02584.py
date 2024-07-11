X, K, D = map(int, input().split())


def sign(x):
    return 1 if x >= 0 else -1


if abs(X) >= D * K:
    ans = X - sign(X) * D * K
else:
    l = abs(X) // D
    mod = abs(X) % D

    residual = K - l

    if residual % 2 == 0:
        ans = mod
    else:
        ans = mod - sign(mod) * D

print(abs(ans))


