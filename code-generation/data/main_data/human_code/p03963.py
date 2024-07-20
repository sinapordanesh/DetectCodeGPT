def answer(n: int, k: int) -> int:
    return k * (k - 1) ** (n - 1)


def main():
    n, k = map(int, input().split())
    print(answer(n, k))


if __name__ == '__main__':
    main()