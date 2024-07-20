def main():
    import sys
    input = sys.stdin.readline

    def same_line(p1, p2, p3):
        c1 = complex(p1[0], p1[1])
        c2 = complex(p2[0], p2[1])
        c3 = complex(p3[0], p3[1])
        a = c2 - c1
        b = c3 - c1
        if a.real * b.imag == a.imag * b.real:
            return 1
        else:
            return 0

    mod = 998244353
    N = int(input())

    if N <= 2:
        print(0)
        exit()

    xy = []
    for _ in range(N):
        x, y = map(int, input().split())
        xy.append((x, y))

    ans = pow(2, N, mod) - N - 1
    ans %= mod
    used = [[0] * N for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1, N):
            if used[i][j]:
                continue
            tmp = [i, j]
            cnt = 2
            for k in range(N):
                if k == i or k == j:
                    continue
                if same_line(xy[i], xy[j], xy[k]):
                    cnt += 1
                    tmp.append(k)
            ans -= pow(2, cnt, mod) - cnt - 1
            ans %= mod
            for a in range(len(tmp)):
                for b in range(a+1, len(tmp)):
                    used[tmp[a]][tmp[b]] = 1
                    used[tmp[b]][tmp[a]] = 1
    print(ans%mod)


if __name__ == '__main__':
    main()
