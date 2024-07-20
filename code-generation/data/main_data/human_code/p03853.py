from typing import List


def answer(h: int, w: int, c: List[str]) -> str:
    result = []
    for i in c:
        for _ in range(2):
            result.append(i)

    return '\n'.join(result)


def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    print(answer(h, w, c))


if __name__ == '__main__':
    main()
