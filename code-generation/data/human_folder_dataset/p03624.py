from string import ascii_lowercase


def answer(s: str) -> str:
    not_in_s = list(set(ascii_lowercase) - set(s))
    if not not_in_s:
        return 'None'
    not_in_s.sort()

    return not_in_s[0]


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()