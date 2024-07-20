from sys import stdin

input = stdin.readline


def solve():
    X = int(input())
    check = (X - 400)//200
    print(8 - check)


if __name__ == '__main__':
    solve()
