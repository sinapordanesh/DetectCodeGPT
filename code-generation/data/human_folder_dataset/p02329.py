import sys
from collections import defaultdict


def main():
    n, v = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    b = tuple(map(int, sys.stdin.readline().split()))
    c = tuple(map(int, sys.stdin.readline().split()))
    d = tuple(map(int, sys.stdin.readline().split()))
    mp = defaultdict(int)
    for val1 in c:
        for val2 in d:
            mp[val1 + val2] += 1
    print(sum(mp[v - val1 - val2] for val1 in a for val2 in b))

if __name__ == '__main__':
    main()

