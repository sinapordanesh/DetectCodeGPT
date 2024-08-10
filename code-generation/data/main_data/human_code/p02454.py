
def equal_range(li, x):
    """Returns a pair of indices (lower_bound, upper_bound).

    >>> equal_range([1, 2, 2, 3], 0)
    (0, 0)
    >>> equal_range([1, 2, 2, 3], 1)
    (0, 1)
    >>> equal_range([1, 2, 2, 3], 2)
    (1, 3)
    >>> equal_range([1, 2, 2, 3], 3)
    (3, 4)
    >>> equal_range([1, 2, 2, 3], 4)
    (4, 4)
    >>> equal_range([2, 2, 2, 2], 2)
    (0, 4)
    """
    def is_lower_bound(i):
        if i == 0:
            return li[i] >= x
        elif i == len(li):
            return li[i-1] < x
        else:
            return (li[i-1] < x and li[i] >= x)

    def is_upper_bound(i):
        if i == 0:
            return li[i] > x
        elif i == len(li):
            return li[i-1] <= x
        else:
            return (li[i-1] <= x and li[i] > x)

    def find_lower(i, j):
        if i == j:
            return i
        mid = i + (j - i) // 2
        if li[mid] >= x:
            return find_lower(i, mid)
        else:
            return find_lower(mid+1, j)

    def find_upper(i, j):
        if i == j:
            return i
        mid = i + (j - i) // 2
        if li[mid] > x:
            return find_upper(i, mid)
        else:
            return find_upper(mid+1, j)

    def search(lo, hi):
        if is_lower_bound(lo) and is_upper_bound(hi):
            return (lo, hi)

        mid = lo + (hi - lo) // 2
        if li[mid] > x:
            return search(lo, mid)
        elif li[mid] < x:
            return search(mid+1, hi)
        else:
            lo = find_lower(lo, mid)
            hi = find_upper(mid+1, hi)
            return search(lo, hi)

    return search(0, len(li))


def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(n == len(a))

    q = int(input())
    for _ in range(q):
        k = int(input())
        x, y = equal_range(a, k)
        print("{} {}".format(x, y))


if __name__ == '__main__':
    run()

