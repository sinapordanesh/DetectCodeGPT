from typing import List


def answer(n: int, m: int, ab_s: List[List[int]]) -> List[int]:
    roads = [0 for _ in range(n)]
    for ab in ab_s:
        a, b = ab
        roads[a - 1] += 1
        roads[b - 1] += 1

    return roads


def main():
    n, m = map(int, input().split())
    ab_s = [list(map(int, input().split())) for _ in range(m)]
    for i in answer(n, m, ab_s):
        print(i)


if __name__ == '__main__':
    main()