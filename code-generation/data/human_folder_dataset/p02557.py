#!/usr/bin/env python3
from collections import Counter
INF = 1e12


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    lA = Counter(A)
    lB = Counter(B)
    if max(Counter(A+B).values()) > N:
        print('No')
        exit()

    C = [0] * (N + 1)
    D = [0] * (N + 1)
    for i in range(N):
        C[i + 1] = lA[i + 1] + C[i]
        D[i + 1] = lB[i + 1] + D[i]
    shift = - INF
    for i in range(1, N + 1):
        shift = max(shift, C[i] - D[i - 1])
    print('Yes')
    ans = (B + B + B)[N-shift:2*N-shift]
    print(' '.join([str(a) for a in ans]))


if __name__ == "__main__":
    main()
