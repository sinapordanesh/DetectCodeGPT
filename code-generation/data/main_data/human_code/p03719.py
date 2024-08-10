def iroha():
    a, b, c = map(int, input().split())

    if a <= c and b >= c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    iroha()

