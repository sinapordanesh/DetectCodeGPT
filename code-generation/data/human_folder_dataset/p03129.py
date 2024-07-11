mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    N, K = map(int, input().split())
    if K <= (N+1) // 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
