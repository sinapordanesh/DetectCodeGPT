#!python3

# input
N, M = list(map(int, input().split()))


def main():
    t = 1900 * M + 100 * (N - M)
    e = 2 ** M
    ans = t * e
    print(ans)


if __name__ == "__main__":
    main()
