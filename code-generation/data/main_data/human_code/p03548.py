def answer(x: int, y: int, z: int) -> int:
    return len(range(y + z * 2, x + 1, y + z))


def main():
    x, y, z = map(int, input().split())
    print(answer(x, y, z))


if __name__ == '__main__':
    main()