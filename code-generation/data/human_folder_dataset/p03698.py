def answer(s: str) -> str:
    return 'yes' if len(s) == len(set(s)) else 'no'


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()