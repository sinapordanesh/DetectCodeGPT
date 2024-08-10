import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    integars = [NLI() for _ in range(N)]

    Kr = [K]
    now_k = 0
    for i in range(32, -1, -1):
        now_bit = (K >> i) & 1
        if now_bit == 0:
            continue
        now_k += pow(2, i)
        Kr.append(now_k - 1)
    ans = 0
    for kr in Kr:
        tmp = 0
        for a, b in integars:
            if (kr | a) == kr:
                tmp += b
        ans = max(ans, tmp)
    print(ans)



if __name__ == "__main__":
    main()