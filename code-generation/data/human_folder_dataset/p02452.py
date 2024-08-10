
def includes(li1, li2):
    """Returns True if li2 is included in li1.
    Assumes li1 and li2 are sorted by ascending order.

    >>> includes([1, 2, 3], [1, 2])
    True
    >>> includes([1, 2, 3], [3, 4])
    False
    """
    def partition(li, x):
        if len(li) == 0:
            return 0
        mid = len(li) // 2
        if li[mid] < x:
            return mid + 1 + partition(li[mid+1:], x)
        elif li[mid] > x:
            return partition(li[:mid], x)
        else:
            return mid

    def binsearch(li, x):
        i = partition(li, x)
        if 0 <= i < len(li):
            return li[i] == x
        else:
            return False

    if len(li1) < len(li2):
        return False
    if len(li2) > 1:
        mid = len(li2) // 2
        i = partition(li1, li2[mid])
        if i >= len(li1) or li2[mid] != li1[i]:
            return False
        else:
            return (includes(li1[:i], li2[:mid])
                    and includes(li1[i+1:], li2[mid+1:]))
    elif len(li2) == 1:
        return binsearch(li1, li2[0])
    else:
        return True


def run():
    n = int(input())
    la = [int(x) for x in input().split()]
    assert(n == len(la))

    m = int(input())
    lb = [int(x) for x in input().split()]
    assert(m == len(lb))

    if includes(la, lb):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    run()

