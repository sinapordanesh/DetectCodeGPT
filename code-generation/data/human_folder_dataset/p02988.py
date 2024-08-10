from typing import Tuple


def answer(n: int, p: Tuple[int]) -> int:
    count = 0
    for i in range(1, n - 1):
        max_ = max(p[i - 1], p[i + 1])
        min_ = min(p[i - 1], p[i + 1])
        if min_ < p[i] < max_:
            count += 1

    return count


def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    print(answer(n, p))


if __name__ == '__main__':
    main()