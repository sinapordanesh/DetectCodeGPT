#!/usr/bin/env python3
# Bitset 2 - Enumeration of Subsets 2


def subset(n, mask):
    for i in range(2**n):
        if i & mask == mask:
            yield i, [v for v in range(n) if i & (1 << v) > 0]


def run():
    n = int(input())
    mask = 0 & 2**n
    for i in input().split()[1:]:
        mask |= 1 << int(i)

    for i, vs in subset(n, mask):
        print("{}:{}".format(i, "".join([" {}".format(v) for v in vs])))


if __name__ == '__main__':
    run()

