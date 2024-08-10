def main() -> None:
    h1, m1, h2, m2, k = map(int, input().split())

    if h1 > h2:
        h2 += 24
    length = (h2*60+m2) - (h1*60+m1)
    print(max(0, length - k))

    return


if __name__ == '__main__':
    main()
