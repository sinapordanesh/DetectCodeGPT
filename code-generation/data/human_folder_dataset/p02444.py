
def rotate(li, b, m, e):
    """Rotate li[b:e] by (m-b).

    >>> rotate([0, 1, 2], 1, 2, 3)
    [0, 2, 1]
    >>> rotate([0], 0, 0, 1)
    [0]
    """
    m = m - b
    return li[:b] + li[b+m:e] + li[b:b+m] + li[e:]


def run():
    n = int(input())
    li = input().split()
    assert(n == len(li))

    q = int(input())
    for _ in range(q):
        b, m, e = [int(x) for x in input().split()]
        li = rotate(li, b, m, e)

    print(" ".join(li))


if __name__ == '__main__':
    run()

