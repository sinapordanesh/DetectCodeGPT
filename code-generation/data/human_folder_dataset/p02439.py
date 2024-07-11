
def min_max(a, b, c):
    """Returns the minimum value and the maximum value
    in a, b, c.

    >>> min_max(1, 2, 3)
    (1, 3)
    >>> min_max(1, 3, 2)
    (1, 3)
    >>> min_max(2, 3, 1)
    (1, 3)
    >>> min_max(2, 1, 3)
    (1, 3)
    >>> min_max(3, 1, 2)
    (1, 3)
    >>> min_max(3, 2, 1)
    (1, 3)
    """
    if a < b:
        if b < c:
            return (a, c)
        elif a < c:
            return (a, b)
        else:
            return (c, b)
    else:
        if a < c:
            return (b, c)
        elif b < c:
            return (b, a)
        else:
            return (c, a)


def run():
    vals = [int(x) for x in input().split()]
    x, y = min_max(*vals)
    print(x, y)


if __name__ == '__main__':
    run()

