import re


def answer(s: str) -> str:
    pattern = r'A[a-z]+C[a-z]+'
    return 'AC' if re.fullmatch(pattern, s) else 'WA'


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()