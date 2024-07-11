from sys import stdin

input = stdin.readline


def solve():
    n = int(input())
    r = n % 1000
    res = 0 if r == 0 else 1000 - r
    print(res)


if __name__ == '__main__':
    solve()
