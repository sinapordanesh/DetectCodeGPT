from typing import List


def answer(n: int, m: int, a: List[str], b: List[str]) -> str:
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            if a[i][j:j + m] == b[0]:
                matched_lines = 1
                for k in range(1, m):
                    if a[i + k][j:j + m] == b[k]:
                        matched_lines += 1
                    else:
                        break
                if matched_lines == m:
                    return 'Yes'

    return 'No'


def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]
    print(answer(n, m, a, b))


if __name__ == '__main__':
    main()