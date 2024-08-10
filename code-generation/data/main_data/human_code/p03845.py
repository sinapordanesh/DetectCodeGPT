from typing import List


def answer(n: int, t: List[int], m: int, pxs: List[List[int]]) -> str:
    result = []
    for px in pxs:
        t_copy = t.copy()
        t_copy[px[0] - 1] = px[1]
        result.append(str(sum(t_copy)))

    return '\n'.join(result)


def main():
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    pxs = [list(map(int, input().split())) for _ in range(m)]
    print(answer(n, t, m, pxs))


if __name__ == '__main__':
    main()
