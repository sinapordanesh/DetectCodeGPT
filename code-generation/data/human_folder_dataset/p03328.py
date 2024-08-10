def answer(a: int, b: int) -> int:
    return sum(range(1, b - a + 1)) - b


def main():
    a, b = map(int, input().split())
    print(answer(a, b))


if __name__ == '__main__':
    main()
