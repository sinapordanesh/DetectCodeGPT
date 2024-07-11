import sys

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

    N, x = in_nn()
    max_n = 2 * N - 1

    if x == 1 or x == max_n:
        print("No")
        exit()

    if x < N:
        ans = []
        pyr = set(range(1, max_n + 1))
        center = [x + 2, x + 1, x, x - 1, x + 3]
        pyr -= set(center)
        pyr = list(pyr)
        t_len = (max_n - 5) // 2
        ans = pyr[:t_len] + center + pyr[t_len:]
    elif x == N:
        ans = list(range(1, max_n + 1))
    elif x > N:
        ans = []
        pyr = set(range(1, max_n + 1))
        center = [x - 2, x - 1, x, x + 1, x - 3]
        pyr -= set(center)
        pyr = list(pyr)
        t_len = (max_n - 5) // 2
        ans = pyr[:t_len] + center + pyr[t_len:]

    print("Yes")
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
