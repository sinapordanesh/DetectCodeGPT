def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b = Input()
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")


main()