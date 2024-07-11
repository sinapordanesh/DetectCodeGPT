from typing import List


def answer(n: int, w: List[str]) -> str:
    if len(set(w)) != len(w):
        return 'No'

    for i in range(1, len(w)):
        if not w[i].startswith(w[i - 1][-1]):
            return 'No'

    return 'Yes'


def main():
    n = int(input())
    w = [input() for _ in range(n)]
    print(answer(n, w))


if __name__ == '__main__':
    main()
