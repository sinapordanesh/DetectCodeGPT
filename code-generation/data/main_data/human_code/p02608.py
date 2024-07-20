import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
from math import sqrt
from collections import defaultdict
def main():
    n = int(input())
    n2 = int(sqrt(n) + 1)
    d1 = defaultdict(int)

    for i1 in range(1, n2):
        for i2 in range(1, n2):
            for i3 in range(1, n2):
                #p = (i1 + i2) ** 2 - (i1 * i2) + i3 * (i1 + i2 + i3)
                p = i1 ** 2 + i2 ** 2 + i3 ** 2 + i1 * i2 + i2 * i3 + i1 * i3
                d1[p] += 1

    for j1 in range(1, n + 1):
        print(d1[j1])

if __name__ == '__main__':
    main()
