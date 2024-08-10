mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    S = input().rstrip('\n')
    w = int(input())
    print(S[::w])


if __name__ == '__main__':
    main()
