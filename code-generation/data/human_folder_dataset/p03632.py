def answer(a: int, b: int, c: int, d: int) -> int:
    return len(set(range(a, b)) & set(range(c, d)))


def main():
    a, b, c, d = map(int, input().split())
    print(answer(a, b, c, d))


if __name__ == '__main__':
    main()