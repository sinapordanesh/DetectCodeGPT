def main():
    a, b, c = map(int, input().split())

    if a + b >= c:
        print(b + c)
    else:
        print(a + 2 * b + 1)


if __name__ == "__main__":
    main()
