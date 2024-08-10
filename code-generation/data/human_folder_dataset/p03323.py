def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")


main()