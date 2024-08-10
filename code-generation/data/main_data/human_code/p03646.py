import sys
import numpy as np

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


def main():
    K = in_n()
    N = 50

    q, r = divmod(K, N)
    ans = np.full(N, N + q)
    cnt = N - r
    ans[:cnt] -= N - (cnt - 1)
    ans[cnt:] += cnt

    print(N)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
