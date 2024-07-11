import sys
import bisect


def main():
    n, K, L, R = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    m = n//2
    ls = [[] for _ in range(m+1)]
    for i in range(1 << m):
        cnt = 0
        val = 0
        for j in range(m):
            if i >> j & 1:
                cnt += 1
                val += a[j]
        ls[cnt].append(val)
    for i in range(m+1):
        ls[i].sort()
    ans = 0
    for i in range(1 << n-m):
        cnt = 0
        val = 0
        for j in range(n-m):
            if i >> j & 1:
                cnt += 1
                val += a[m+j]
        if K-m <= cnt <= K:
            ans += bisect.bisect_right(ls[K-cnt], R-val) - bisect.bisect_right(ls[K-cnt], L-val-1)
    print(ans)


if __name__ == '__main__':
    main()

