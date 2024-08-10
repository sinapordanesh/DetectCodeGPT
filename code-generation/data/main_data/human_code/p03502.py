def is_harshad_number(x: int) -> bool:
    dividend = x
    sum_of_digits = 0

    for _ in range(len(str(x))):
        x, mod = divmod(x, 10)
        sum_of_digits += mod

    return dividend % sum_of_digits == 0


def answer(x: int) -> str:
    return 'Yes' if is_harshad_number(x) else 'No'


def main():
    x = int(input())
    print(answer(x))


if __name__ == '__main__':
    main()