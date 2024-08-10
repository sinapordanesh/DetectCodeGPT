def answer(n: int, k: int) -> int:
    current_num = 1
    for _ in range(n):
        current_num = min(current_num * 2, current_num + k)

    return current_num


def main():
    n =int(input())
    k = int(input())
    print(answer(n, k))


if __name__ == '__main__':
    main()
