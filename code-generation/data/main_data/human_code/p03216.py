import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S = input()
    Q = int(readline())
    K = list(map(int, readline().split()))

    for q in range(Q):
        k = K[q]
        res = 0
        cnt = [0] * 3
        for i in range(k):
            cur = S[i]
            if cur == "D":
                cnt[0] += 1
            elif cur == "M":
                cnt[1] += 1
                cnt[2] += cnt[0]
            elif cur == "C":
                res += cnt[2]

        for i in range(k, N):
            prev = S[i - k]
            cur = S[i]
            if prev == "D":
                cnt[0] -= 1
                cnt[2] -= cnt[1]
            elif prev == "M":
                cnt[1] -= 1

            if cur == "D":
                cnt[0] += 1
            elif cur == "M":
                cnt[1] += 1
                cnt[2] += cnt[0]
            elif cur == "C":
                res += cnt[2]
        print(res)


if __name__ == '__main__':
    main()
