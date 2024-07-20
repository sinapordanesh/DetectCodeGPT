import sys
from collections import Counter

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = Counter(A)
    ans = 0
    for i in range(10 ** 5 + 1):
        ans = max(ans, C[i - 1] + C[i] + C[i + 1])
    print(ans)


if __name__ == '__main__':
    main()
