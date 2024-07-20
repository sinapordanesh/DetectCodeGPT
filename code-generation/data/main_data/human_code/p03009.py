mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, H, D = map(int, input().split())
    imos = [0] * (H+2)
    ans = [0] * (H+1)
    M = 0
    f = 1
    for i in range(1, N+1):
        f = (f * i)%mod
        M = (M + f)%mod
    imos[1] += f
    imos[D+1] -= f
    for i in range(1, H):
        ans[i] = (ans[i-1] + imos[i])%mod
        imos[i+1] = (imos[i+1] + (ans[i] * M)%mod)%mod
        if i+D+1 <= H:
            imos[i+D+1] = (imos[i+D+1] - (ans[i] * M)%mod)%mod
    print((ans[H-1] + imos[H])%mod)


if __name__ == '__main__':
    main()
