import sys
from itertools import permutations

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())
    A.sort()

    vec1 = [0] * N
    vec2 = [0] * N
    for i in range(N - 1):
        if i % 2 == 0:
            vec1[i] += 1
            vec1[i + 1] -= 1
            vec2[i] -= 1
            vec2[i + 1] += 1
        else:
            vec1[i] -= 1
            vec1[i + 1] += 1
            vec2[i] += 1
            vec2[i + 1] -= 1

    vec1.sort()
    vec2.sort()

    ans1 = ans2 = 0
    for a, v1, v2 in zip(A, vec1, vec2):
        ans1 += a * v1
        ans2 += a * v2

    print(max(ans1, ans2))
    return


if __name__ == '__main__':
    main()
