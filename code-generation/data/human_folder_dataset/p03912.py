import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    X = list(map(int, input().split()))

    MOD = [defaultdict(int) for _ in range(m + 1)]
    cnt = defaultdict(int)
    for x in X:
        MOD[x % m][x] += 1
        cnt[x % m] += 1

    res = cnt[0] // 2
    if m % 2 == 0:
        res += cnt[m // 2] // 2

    for i in range(1, (m + 1) // 2):
        res += min(cnt[i], cnt[m - i])

        if cnt[i] > cnt[m - i]:
            diff = (cnt[i] - cnt[m - i]) // 2
            for v in MOD[i].values():
                if diff == 0:
                    break
                t = min(diff, v // 2)
                diff -= t
                res += t
        elif cnt[i] < cnt[m - i]:
            diff = (cnt[m - i] - cnt[i]) // 2
            for v in MOD[m - i].values():
                if diff == 0:
                    break
                t = min(diff, v // 2)
                diff -= t
                res += t

    print(res)


if __name__ == '__main__':
    resolve()
