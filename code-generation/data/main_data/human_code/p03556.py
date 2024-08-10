import math


def answer(n: int) -> int:
    return int(math.sqrt(n)) ** 2


def main():
    n = int(input())
    print(answer(n))


if __name__ == '__main__':
    main()