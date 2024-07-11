import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N = int(input())

    for h in range(1, 3501):
        for n in range(1, 3501):
            if 4 * n * h - N * n - N * h == 0:
                continue
            q, r = divmod(N * n * h, 4 * n * h - N * n - N * h)
            if r == 0 and q > 0:
                print(h, n, q)
                return


if __name__ == '__main__':
    main()
