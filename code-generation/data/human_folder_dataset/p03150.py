import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    S = input()
    key = "keyence"
    if key in S:
        print("YES")
        return

    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            if S[:i] + S[j:] == key:
                print("YES")
                return

    print("NO")
    return


if __name__ == "__main__":
    main()
