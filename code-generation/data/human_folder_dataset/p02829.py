#!/usr/bin/env python3
import sys
from itertools import chain


def solve(A: int, B: int):
    answer = 6 - A - B
    return answer


def main():
    tokens = chain(*(line.split() for line in sys.stdin))
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    answer = solve(A, B)
    print(answer)


if __name__ == "__main__":
    main()
