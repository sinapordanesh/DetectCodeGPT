from typing import List


def answer(n: int, lrs: List[List[int]]) -> int:
    number_of_people_sitting = 0
    for lr in lrs:
        l, r = lr
        number_of_people_sitting += r - l + 1

    return number_of_people_sitting


def main():
    n = int(input())
    lrs = [map(int, input().split()) for _ in range(n)]
    print(answer(n, lrs))


if __name__ == '__main__':
    main()