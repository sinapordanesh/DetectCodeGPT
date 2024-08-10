#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, exit, maxsize


def find(n, data):
    temp = [0] * (n * (n+1) // 2)
    maximum = -maxsize

    for row in data:
        index = 0
        num_cell = 1

        for end in range(n, -1, -1):
            for i in range(end):
                k = index + i

                now = sum(row[i:i+num_cell])
                if temp[k] < 0:
                    temp[k] = now
                else:
                    temp[k] += now

                if maximum < temp[k]:
                    maximum = temp[k]

            index += end
            num_cell += 1

    return maximum


def main(readline=stdin.readline):
    n = int(readline())

    a = []
    for _ in range(n):
        a.append([int(s) for s in readline().split()])

    print(find(n, a))
    exit()


if __name__ == '__main__':
    main()