def answer(s: str) -> int:
    if len(s) % 2 == 1:
        s += ' '

    for _ in range(len(s) // 2):
        s = s[:-2]
        l = len(s)
        middle = l // 2

        if s[:middle] == s[middle:]:
            return l


def main():
    s = input()
    print(answer(s))


if __name__ == '__main__':
    main()