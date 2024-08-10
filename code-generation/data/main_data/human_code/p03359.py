def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()

    if a - b <= 0:
        print(a)
    else:
        print(a - 1)


main()