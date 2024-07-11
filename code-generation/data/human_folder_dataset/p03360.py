def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    a, b, c = sorted(Input())
    k = int(input())

    for i in range(k):
        c *= 2
    print(a+b+c)


main()