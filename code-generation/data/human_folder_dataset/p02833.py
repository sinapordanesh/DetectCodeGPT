import sys
from itertools import accumulate, repeat, takewhile
from operator import mul


def main():
    N = int(next(sys.stdin.buffer))
    if N % 2:
        print(0)
        return
    print(sum(N // x for x in takewhile(lambda x: x <= N, accumulate(repeat(5), mul, initial=10))))


if __name__ == '__main__':
    main()
