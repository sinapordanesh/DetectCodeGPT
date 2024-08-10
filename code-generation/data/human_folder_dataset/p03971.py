import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, a, b = input_int_list()
    S = input()
    passed = 0
    oversea = 0
    for s in S:
        if s == "a" and passed < a + b:
            passed += 1
            print("Yes")
        elif s == "b" and passed < a + b and oversea < b:
            oversea += 1
            passed += 1
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
