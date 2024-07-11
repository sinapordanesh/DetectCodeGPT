import sys

input = sys.stdin.buffer.readline
in_n = lambda: int(input())
in_nn = lambda: map(int, input().split())
in_s = lambda: input().rstrip().decode('utf-8')
in_map = lambda: [s == ord('.') for s in input() if s != ord('\n')]

MOD = 10**9 + 7
INF = 8 * 10**18


def main():

    _, s, _ = in_s().split()

    print("A" + s[0] + "C")


if __name__ == '__main__':
    main()
