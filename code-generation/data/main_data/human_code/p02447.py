
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])


def sort(li):
    """Sort a list of Point(x, y) ascending order

    >>> sort([Point(x=2, y=1), Point(x=1, y=0)])
    [Point(x=1, y=0), Point(x=2, y=1)]
    >>> sort([Point(x=1, y=4), Point(x=1, y=3)])
    [Point(x=1, y=3), Point(x=1, y=4)]
    """
    li = sorted(li, key=lambda p: p.y)
    return sorted(li, key=lambda p: p.x)


def run():
    n = int(input())
    ps = []
    for _ in range(n):
        x, y = [int(i) for i in input().split()]
        ps.append(Point(x, y))

    for p in sort(ps):
        print("{} {}".format(p.x, p.y))


if __name__ == '__main__':
    run()

