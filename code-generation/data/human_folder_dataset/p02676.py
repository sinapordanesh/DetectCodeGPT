import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    k = int(readline())
    s = str(readline().rstrip().decode('utf-8'))
    print(s if len(s) <= k else s[:k] + "...")


if __name__ == '__main__':
    solve()
