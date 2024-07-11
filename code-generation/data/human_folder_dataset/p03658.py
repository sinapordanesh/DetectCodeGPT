from typing import List


def answer(n: int, k: int, l: List[int]) -> int:
    l.sort(reverse=True)
    return sum(l[:k])


def main():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    print(answer(n, k, l))


if __name__ == '__main__':
    main()
