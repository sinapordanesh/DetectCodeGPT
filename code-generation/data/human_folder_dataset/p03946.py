import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, T = map(int, readline().split())
    A = list(map(int, readline().split()))

    L = []
    Max = 0
    Min = A[0]

    for i in range(1, N):
        if A[i] < Min:
            Min = A[i]
        if A[i] - Min > Max:
            Max = A[i] - Min
        L.append(A[i] - Min)
    print(L.count(Max))

if __name__ == '__main__':
    main()
