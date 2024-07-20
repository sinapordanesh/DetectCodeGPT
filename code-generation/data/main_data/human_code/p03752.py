import sys

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))

    if N == K:
        mask = [1] * N

        print(calc(N, a, mask))
        return

    ans = sys.maxsize
    for i in range(1 << N):
        mask = [i >> j & 1 for j in range(N)]
        if sum(mask) < K: continue
        mask.reverse()

        ans = min(ans, calc(N, a, mask))

    print(ans)
    return

def calc(N, a, mask):
    ans = 0
    m = a[0]
    for i in range(1, N):
        m = max(m, a[i - 1])
        if mask[i] == 0:continue
        if m < a[i]:
            continue
        else:
            v = m - a[i] + 1
            ans += v
            m = a[i] + v

    return ans

if __name__ == '__main__':
    main()