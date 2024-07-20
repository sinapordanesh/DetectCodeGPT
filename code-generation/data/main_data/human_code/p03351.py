import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


def main():

    a, b, c, d = in_nn()

    if abs(a - c) <= d or (abs(a - b) <= d and abs(b - c) <= d):
        print('Yes')
    else:
        print("No")


if __name__ == '__main__':
    main()
