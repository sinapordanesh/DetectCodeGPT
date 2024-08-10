from typing import List


def answer(n: int, x: int, m: List[int]) -> int:
    x -= sum(m)
    count = len(m)
    count += x // min(m)

    return count


def main():
    n, x = map(int, input().split())
    m = [int(input()) for _ in range(n)]
    print(answer(n, x, m))


if __name__ == '__main__':
    main()