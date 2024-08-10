
def unique(li):
    """Returns a list of unique elements in ordered list li

    >>> unique([1, 1])
    [1]
    >>> unique([1, 2])
    [1, 2]
    """
    return [li[i] for i in range(len(li)) if i == 0 or li[i] > li[i-1]]


def run():
    n = int(input())
    li = [int(x) for x in input().split()]
    assert(n == len(li))

    print(" ".join([str(x) for x in unique(li)]))


if __name__ == '__main__':
    run()

