def mapt(fn, *args):
    return tuple(map(fn, *args))


def main():
    s = mapt(int, input().split("/"))
    print("Heisei" if s <= (2019, 4, 30) else "TBD")

main()