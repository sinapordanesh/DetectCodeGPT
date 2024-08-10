def answer(n: int, s: str) -> int:
    while 'DI' in s:
        s = s.replace('DI', '')

    return s.count('I')


def main():
    n = int(input())
    s = input()
    print(answer(n, s))


if __name__ == '__main__':
    main()