import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n = int(readline())
    t = 1
    m = 10 ** 18
    for v in sorted(list(map(int, readline().split()))):
        t *= v
        if t > m:
            print(-1)
            exit()
    print(t)


if __name__ == '__main__':
    solve()
