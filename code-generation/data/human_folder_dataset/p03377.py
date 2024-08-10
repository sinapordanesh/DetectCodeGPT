def main():
    a, b, x = map(int, input().split())

    if a <= x <= a + b:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
