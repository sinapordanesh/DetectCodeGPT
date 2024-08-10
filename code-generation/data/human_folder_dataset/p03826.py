import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A,B,C,D=map(int, readline().split())
    print(max(A*B,C*D))

if __name__ == '__main__':
    main()
