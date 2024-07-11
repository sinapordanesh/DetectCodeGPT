def answer(a: int, b: int) -> int:
    count = 0
    for i in range(a, b + 1):
        i_str = str(i)
        if i_str[0] == i_str[-1] and i_str[1] == i_str[-2]:
            count += 1

    return count


def main():
    a, b = map(int, input().split())
    print(answer(a, b))


if __name__ == '__main__':
    main()
