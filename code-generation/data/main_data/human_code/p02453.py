
from bisect import bisect_left


def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(n == len(a))

    q = int(input())
    for _ in range(q):
        k = int(input())
        i = bisect_left(a, k)
        print(i)


if __name__ == '__main__':
    run()

