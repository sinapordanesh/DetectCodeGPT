def answer(n: int) -> str:
    temp = n
    sum_of_digits = 0

    while 0 < temp:
        temp, mod = divmod(temp, 10)
        sum_of_digits += mod

    return 'Yes' if n % sum_of_digits == 0 else 'No'


def main():
    n = int(input())
    print(answer(n))


if __name__ == '__main__':
    main()