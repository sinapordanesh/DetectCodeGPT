import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    S = input().split('T')
    x, y = map(int, input().split())

    X = []
    Y = []
    flag = 0
    for s in S:
        if flag == 0:
            X.append(len(s))
        else:
            Y.append(len(s))
        flag ^= 1

    A = set()
    A.add(X[0])
    for i in X[1:]:
        tmp = set()
        for a in A:
            tmp.add(a + i)
            tmp.add(a - i)
        A = tmp

    B = set()
    B.add(0)
    for j in Y:
        tmp = set()
        for b in B:
            tmp.add(b + j)
            tmp.add(b - j)
        B = tmp

    if x in A and y in B:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
