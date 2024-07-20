def number_of_divisors(x: int) -> int:
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1

    return count


def answer(n: int) -> int:
    if n < 105:
        return 0

    count = 0
    for i in range(105, n + 1, 2):
        if number_of_divisors(i) == 8:
            count += 1

    return count


def main():
    n = int(input())
    print(answer(n))


if __name__ == '__main__':
    main()
