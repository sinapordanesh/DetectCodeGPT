def func(n: int) -> int:
    return n // 2 if n % 2 == 0 else n * 3 + 1


def answer(s: int) -> int:
    sequence_a = [s]
    while True:
        num = func(sequence_a[-1])
        if num in sequence_a:
            return len(sequence_a) + 1
        sequence_a.append(num)


def main():
    s = int(input())
    print(answer(s))


if __name__ == '__main__':
    main()
