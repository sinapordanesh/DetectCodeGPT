import sys
import itertools


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m, x = list(map(int, readline().split()))
    c = [list(map(int, readline().split())) for _ in range(n)]
    mv = 10 ** 10
    for v in itertools.product([True, False], repeat=n):
        score = [0] * m
        amt = 0
        for i, vv in enumerate(v):
            if vv:
                amt += c[i][0]
                for j in range(m):
                    score[j] += c[i][j+1]
                b = True
                for sv in score:
                    if sv < x:
                        b = False
                        break
                if b:
                    mv = min(mv, amt)
    print(mv if mv != 10 ** 10 else -1)


if __name__ == '__main__':
    solve()
