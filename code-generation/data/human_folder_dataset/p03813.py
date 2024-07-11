import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X = int(readline())
    if X<1200:
        print('ABC')
    else:
        print('ARC')

if __name__ == '__main__':
    main()
