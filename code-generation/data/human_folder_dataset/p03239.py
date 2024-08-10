from typing import List


def answer(n: int, t: int, cts: List[List[int]]) -> int:
    costs = [route[0] for route in cts if route[1] <= t]
    if not costs:
        return -1

    return min(costs)


def main():
    n, t = map(int, input().split())
    cts = [list(map(int, input().split())) for _ in range(n)]
    ans = answer(n, t, cts)
    print(ans if ans != -1 else 'TLE')


if __name__ == '__main__':
    main()
